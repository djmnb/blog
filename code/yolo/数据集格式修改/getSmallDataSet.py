import os
import shutil
import random
import argparse

def move_files_with_limit(source_dir, target_dir, count):
    """
    从 source_dir 的 images 文件夹中随机选择指定数量的图片文件，
    并将这些文件及对应的标签文件复制到 target_dir 的 labels 和 images 文件夹中。

    :param source_dir: 源目录，包含 labels 和 images 文件夹
    :param target_dir: 目标目录，将复制的文件保存到此处
    :param count: 要复制的文件数量
    """
    # 确保 source_dir 存在
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory {source_dir} does not exist.")

    labels_source = os.path.join(source_dir, "labels")
    images_source = os.path.join(source_dir, "images")

    if not os.path.exists(labels_source) or not os.path.exists(images_source):
        raise ValueError("Source directory must contain 'labels' and 'images' folders.")

    # 获取 images 文件列表
    images_files = sorted(os.listdir(images_source))

    # 检查是否有足够的图片文件
    if len(images_files) < count:
        raise ValueError(f"Not enough image files to move. Requested: {count}, Found: {len(images_files)}")

    # 随机选择指定数量图片文件
    selected_images = random.sample(images_files, count)

    # 创建目标文件夹
    labels_target = os.path.join(target_dir, "labels")
    images_target = os.path.join(target_dir, "images")

    os.makedirs(labels_target, exist_ok=True)
    os.makedirs(images_target, exist_ok=True)

    # 复制文件
    for image_file in selected_images:
        # Copy image file
        src_image_path = os.path.join(images_source, image_file)
        tgt_image_path = os.path.join(images_target, image_file)
        shutil.copy(src_image_path, tgt_image_path)

        # Derive label file name and copy if it exists
        base_name = os.path.splitext(image_file)[0]
        label_file = base_name + ".txt"  # 假设标签文件扩展名是 .txt
        src_label_path = os.path.join(labels_source, label_file)
        if os.path.exists(src_label_path):
            tgt_label_path = os.path.join(labels_target, label_file)
            shutil.copy(src_label_path, tgt_label_path)

    print(f"Successfully moved {count} images and their labels to {target_dir}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move a specified number of image and label files to a target directory.")
    parser.add_argument("--s", type=str, help="Source directory containing 'labels' and 'images' folders.")
    parser.add_argument("--t", type=str, help="Target directory to save selected files.")
    parser.add_argument("--c", type=int, help="Number of files to move.")

    args = parser.parse_args()

    move_files_with_limit(args.s, args.t, args.c)

