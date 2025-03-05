import os
import shutil

def copy_data(source_dir, target_dir, isok_func, nums):
    """
    将指定源目录中的图片和标签文件根据过滤函数和数量限制复制到目标目录。
    
    :param source_dir: 源目录，应该包含 images 和 labels 子目录
    :param target_dir: 目标目录，目标路径将包含 images 和 labels 子目录
    :param isok_func: 用于过滤文件的函数，接收文件路径返回布尔值
    :param nums: 限定需要复制的文件数量
    """
    # 检查源目录和目标目录的基本结构
    images_dir = os.path.join(source_dir, 'images')
    labels_dir = os.path.join(source_dir, 'labels')
    
    if not os.path.isdir(images_dir) or not os.path.isdir(labels_dir):
        raise ValueError("源目录必须包含 'images' 和 'labels' 子目录")
    
    # 获得目标目录的基本结构
    target_images_dir = os.path.join(target_dir, 'images')
    target_labels_dir = os.path.join(target_dir, 'labels')
    
    # 如果目录存在就删掉
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    # 创建目标目录
    os.makedirs(target_images_dir, exist_ok=True)
    os.makedirs(target_labels_dir, exist_ok=True)
    
    # 创建目标目录结构
    # os.makedirs(os.path.join(target_dir, 'images'), exist_ok=True)
    # os.makedirs(os.path.join(target_dir, 'labels'), exist_ok=True)
    
    # 获取源目录中的所有图片和标签文件
    image_files = set(f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg')))
    label_files = set(f for f in os.listdir(labels_dir) if f.endswith('.txt'))
    
    # 图片排序
    image_files = sorted(image_files)
    
    
    # 限制文件数量，按文件名进行配对
    num_copied = 0
    for image_file in image_files:
        label_file = image_file.replace(os.path.splitext(image_file)[1], '.txt')
        if label_file in label_files:
            # 形成图片和标签的路径
            image_path = os.path.join(images_dir, image_file)
            label_path = os.path.join(labels_dir, label_file)
            
            # 判断是否符合过滤条件
            if isok_func(image_path, label_path) or isok_func is None:
                # 复制图片和标签文件
                shutil.copy(image_path, os.path.join(target_dir, 'images', image_file))
                shutil.copy(label_path, os.path.join(target_dir, 'labels', label_file))
                num_copied += 1
                
                # 如果复制的数量达到限制，退出
                if num_copied >= nums:
                    break

if __name__ == "__main__":
    source_dir = "/data/DJM/VOC/yolo/2007/train"
    target_dir = "/data/DJM/VOC/yolo/2007/train-1"
    def isok_func(image_path, label_path):
        # 在这里实现你的过滤逻辑
        # 例如，你可以检查标签文件中是否包含特定的类别的物体
        with open(label_path, 'r') as f:
            if len(f.readlines()) == 1:
                return True
        return False
    nums = 16
    copy_data(source_dir, target_dir, isok_func, nums)