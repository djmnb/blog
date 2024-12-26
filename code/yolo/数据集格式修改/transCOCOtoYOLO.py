import os
import json
import zipfile
import shutil

def extract_coco_archives(data_dir, extract_dir):
    """
    解压 COCO 数据集中的所有压缩包到指定目录。
    如果目标目录已经存在，则跳过解压。

    :param data_dir: COCO 数据集压缩包所在的目录
    :param extract_dir: 解压后的目标目录
    """
    if os.path.exists(extract_dir):
        print(f"Directory {extract_dir} already exists. Skipping extraction.")
        return

    os.makedirs(extract_dir, exist_ok=True)  # 创建解压目标目录

    for file_name in os.listdir(data_dir):
        if file_name.endswith('.zip'):
            zip_path = os.path.join(data_dir, file_name)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
    print(f"Extracted all COCO archives to {extract_dir}.")


import logging

def convert_coco_to_yolo(coco_dir, output_dir, overwrite=False):
    """
    优化版 COCO 转 YOLO 格式转换器。

    :param coco_dir: 解压后的 COCO 数据集路径
    :param output_dir: YOLO 格式数据保存的目标目录
    :param overwrite: 是否覆盖已存在的文件
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    annotations_dir = os.path.join(coco_dir, 'annotations')
    splits = ['train', 'val']  # 仅处理 train 和 val

    for split in splits:
        coco_json_path = os.path.join(annotations_dir, f'instances_{split}2017.json')
        if not os.path.exists(coco_json_path):
            logging.warning(f"Annotation file {coco_json_path} does not exist. Skipping {split}.")
            continue

        yolo_images_dir = os.path.join(output_dir, split, 'images')
        yolo_labels_dir = os.path.join(output_dir, split, 'labels')
        os.makedirs(yolo_images_dir, exist_ok=True)
        os.makedirs(yolo_labels_dir, exist_ok=True)

        # 加载 COCO 标注数据
        with open(coco_json_path, 'r') as f:
            coco_data = json.load(f)

        # 创建类别映射
        category_id_mapping = {cat['id']: idx for idx, cat in enumerate(coco_data['categories'])}

        # 按 image_id 分组标注数据
        annotations_by_id = {}
        for ann in coco_data['annotations']:
            annotations_by_id.setdefault(ann['image_id'], []).append(ann)

        # 遍历图片信息
        for image_info in coco_data['images']:
            image_id = image_info['id']
            file_name = image_info['file_name']
            src_image_path = os.path.join(coco_dir, f'{split}2017', file_name)
            dest_image_path = os.path.join(yolo_images_dir, file_name)

            # 检查图片文件是否存在并复制
            if not os.path.exists(src_image_path):
                logging.warning(f"Image file {src_image_path} does not exist. Skipping.")
                continue

            if not os.path.exists(dest_image_path) or overwrite:
                shutil.copy(src_image_path, dest_image_path)

            # 获取该图片对应的所有标注
            annotations = annotations_by_id.get(image_id, [])

            # 生成 YOLO 格式标注文件
            yolo_label_path = os.path.join(yolo_labels_dir, os.path.splitext(file_name)[0] + '.txt')
            with open(yolo_label_path, 'w') as label_file:
                inv_width = 1.0 / image_info['width']
                inv_height = 1.0 / image_info['height']
                for ann in annotations:
                    category_id = category_id_mapping.get(ann['category_id'], -1)
                    if category_id == -1:
                        logging.warning(f"Category ID {ann['category_id']} not found in categories. Skipping annotation.")
                        continue

                    bbox = ann['bbox']
                    x_min, y_min, box_width, box_height = bbox

                    # 检查边界框合法性
                    if box_width <= 0 or box_height <= 0:
                        logging.warning(f"Invalid bounding box {bbox} for image {file_name}. Skipping annotation.")
                        continue

                    x_center = (x_min + box_width / 2) * inv_width
                    y_center = (y_min + box_height / 2) * inv_height
                    width = box_width * inv_width
                    height = box_height * inv_height

                    # 检查值是否在 0-1 范围内
                    if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 0 < width <= 1 and 0 < height <= 1):
                        logging.warning(f"Bounding box {bbox} out of range for image {file_name}. Skipping annotation.")
                        continue

                    label_file.write(f"{category_id} {x_center} {y_center} {width} {height}\n")

        logging.info(f"Converted COCO {split} annotations to YOLO format in {output_dir}/{split}.")


# 示例调用
extract_coco_archives('/data/DJM/coco', '/data/DJM/coco/coco_extracted')
convert_coco_to_yolo('/data/DJM/coco/coco_extracted', '/data/DJM/coco/yolo')