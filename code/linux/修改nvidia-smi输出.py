#!/usr/bin/env python3
import subprocess
import sys

def get_nvidia_smi_output():
    """调用 nvidia-smi 并返回其原始输出(字符串)。"""
    try:
        result = subprocess.run(['DJMtest'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode != 0:
            sys.exit(result.returncode)
        return result.stdout
    except Exception as e:
        sys.exit(1)

def get_user_from_pid(pid):
    """
    通过 ps 命令获取指定 PID 的用户名。
    """
    cmd = ['ps', '-p', str(pid), '-o', 'user=']
    try:
        result = subprocess.check_output(cmd,
                                         stderr=subprocess.STDOUT,
                                         text=True)
        user = result.strip()
        if user:
            return user
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def split_output_into_sections(nvidia_output):
    """
    将 nvidia-smi 的输出分成两部分：
    1. gpu_info_lines: 上半部分（包括 GPU 信息、表头）
    2. processes_lines: 下半部分（Process 表）
    """
    lines = nvidia_output.split('\n')
    gpu_info_lines = []
    processes_lines = []
    processes_section_found = False

    for line in lines:
        if line.strip().startswith("| Processes:"):
            processes_section_found = True
            gpu_info_lines.append(line)  # 这行通常是 "| Processes: ..."
            continue
        if processes_section_found:
            processes_lines.append(line)
        else:
            gpu_info_lines.append(line)

    return gpu_info_lines, processes_lines

def parse_process_entries(processes_lines):
    """
    从 Processes 区域提取每个进程的信息，并返回一个列表：
    [
      {
        'gpu_id': 0,
        'pid': 1234,
        'usage': 1000,   # MiB
        'name': 'python'
      },
      ...
    ]
    不同 nvidia-smi 版本的列对齐可能略有差别，这里做一个简化示例。
    """
    entries = []
    for line in processes_lines:
        striped = line.strip()
        # 跳过表格分割线、表头、空白等
        if (striped.startswith('+') or 
            striped.startswith('|==') or
            'PID' in striped or
            'GPU Memory' in striped or
            'No running processes found' in striped or
            not striped.startswith('|')):
            continue

        # 示例行： "|    0    183431      C   .../envs/GAS/bin/python  10537MiB |"
        parts = striped.strip('|').split()
        if len(parts) < 5:
            continue

        gpu_id = parts[0]
        pid = parts[1]
        # usage 通常是最后一个，形如 "10537MiB"
        type = parts[2]
        
        usage_str = parts[-1]
        usage = 0
        if usage_str.endswith("MiB"):
            try:
                usage = int(usage_str.replace("MiB", ""))
            except ValueError:
                usage = 0

        # 进程名一般位于 parts[3 : -1] (因为 parts[2] 是进程类型 C/G 等)
        # 这里做简化处理
        process_name = parts[3]
        
        entries.append({
            'gpu_id': gpu_id,
            'pid': pid,
            "type": type,  # 示例，实际可能是 "C/G"
            'usage': usage,
            'name': process_name
        })

    return entries

def rebuild_process_table(process_entries):
    """
    按照 nvidia-smi 的格式，重建进程表。如果没有进程，则显示 “No running processes found”。
    """
    
    lines = []
    
    lines.append("|  GPU       PID   Type   Process name                             Usage      |")
    lines.append("|=============================================================================|")

    
    if not process_entries:
        lines.extend([
            "| No running processes found                                                  |",
            "+-----------------------------------------------------------------------------+"
        ])
        return lines

   
    for e in process_entries:
        # 这里无法完全对齐原始的列宽，仅示例，可自行调整
        # GPU, PID, 假设 Type 一律用 'C' （或你需要保留的话，就在 parse 时取到）
        # Name (尽量往左对齐), Usage
        lines.append(f"|  {e['gpu_id']:>3} {e['pid']:>9}      C   {e['name']:<35}{e['usage']:>6}MiB |")

    lines.append("+-----------------------------------------------------------------------------+")
    return lines

def update_gpu_memory_usage(gpu_info_lines, new_usage, new_per=0):
    """
    将 GPU Info 中的 “xxxMiB / yyyMiB” 的 xxx 改成 new_usage。
    仅在检测到 "Memory-Usage" 行时做简单替换。
    这里只针对单卡做演示，多卡请自行扩展。
    """
    updated_lines = []
    for line in gpu_info_lines:
        if "Default" in line and "MiB" in line:
            # 简易做法：找 "MiB /" 并替换前面的数字
            parts = line.split('|')
            if len(parts) < 3:
                updated_lines.append(line)
                continue
            segment = parts[2]  # 形如 "  11248MiB / 32510MiB "
            per = parts[3]
            # 如果要更精确，可用正则，或做更严格的 split
            if "MiB /" in segment:
                left_part = segment.split("MiB /")[0]  # "  11248"
                # 用新的 usage 替换
                new_segment = segment.replace(left_part, f"{new_usage:7d}")
                parts[2] = new_segment
                
                if new_per:
                    newp = per.split("%")[0]
                    parts[3] = per.replace(newp, f"{0:>7d}")
                new_line = "|".join(parts)
                updated_lines.append(new_line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    return updated_lines

def modify_output(gpu_info_lines, processes_lines, djm_user="DJM"):
    """
    根据需求进行修改：
      1) 如果只有 DJM，清空显存(把 GPU Info 显存设为 0，进程表也改为 usage=0 或不显示)
      2) 如果同时有 DJM 和其他用户，隐藏 DJM，DJM 占用的显存平均分给其他用户
      3) 如果没有 DJM，则保持原状
    """
    entries = parse_process_entries(processes_lines)
    if not entries:
        # 无进程，直接返回原样
        return "\n".join(gpu_info_lines + processes_lines)

    # 区分 DJM 与其他
    djm_entries = []
    other_entries = []
    total_djm_usage = 0

    for e in entries:
        user = get_user_from_pid(e['pid'])
        if user == djm_user:
            djm_entries.append(e)
            total_djm_usage += e['usage']
        else:
            other_entries.append(e)

    # 1) 没有 DJM
    if not djm_entries:
        # 保持原状
        return "\n".join(gpu_info_lines + processes_lines)

    # 2) 只有 DJM
    if djm_entries and not other_entries:
        # 把 GPU Info 显存 usage 改为 0
        new_gpu_info = update_gpu_memory_usage(gpu_info_lines, 0, 1)
        # 如果要隐藏进程表：只需返回 “No running processes found”
        # 如果要显示，就把所有 djm_entries usage = 0
       
        new_process_table = rebuild_process_table(None)
        return "\n".join(new_gpu_info + new_process_table)

    # 3) 同时有 DJM 和其他
    # 隐藏 DJM；把 total_djm_usage 平分给其他进程
    n_other = len(other_entries)
    if n_other > 0:
        added_each = total_djm_usage // n_other
        for o in other_entries:
            o['usage'] += added_each

    # 重新计算所有 other_entries 的总 usage
    new_total_usage = sum([o['usage'] for o in other_entries])

    # 更新 GPU Info 显存
    new_gpu_info = update_gpu_memory_usage(gpu_info_lines, new_total_usage)

    # 只保留其他用户进程
    new_process_table = rebuild_process_table(other_entries)

    return "\n".join(new_gpu_info + new_process_table)

def main():
    # 1. 获取原始输出
    original_output = get_nvidia_smi_output()

    try:
        # 2. 拆分出 GPU 信息、进程表
        gpu_info_lines, processes_lines = split_output_into_sections(original_output)

        # 3. 根据需求修改
        final_output = modify_output(gpu_info_lines, processes_lines, djm_user="DJM")
        # 4. 输出结果
        print(final_output)
    except Exception as e:
        print(original_output)

if __name__ == "__main__":
    main()
