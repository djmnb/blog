import os
import tarfile
import xml.etree.ElementTree as ET
import shutil


def extract_all_tar_files(src_dir, extract_dir):
    """
    解压一个目录下的所有 .tar 文件到目标目录。
    如果目标目录已存在相应子目录，则跳过解压。

    :param src_dir: 包含 .tar 文件的目录
    :param extract_dir: 解压后的目标目录
    """

    if os.path.exists(extract_dir):
        print(f"Directory {extract_dir} already exists. Skipping ")
        return

    os.makedirs(extract_dir)

    for file_name in os.listdir(src_dir):
        if file_name.endswith(".tar"):
            tar_path = os.path.join(src_dir, file_name)

            with tarfile.open(tar_path, "r:*") as tar_ref:
                tar_ref.extractall(extract_dir)
            print(f"Extracted {file_name} to {extract_dir}.")


def parse_voc_annotation(annotation_path, classes):
    """
    解析 VOC 的 XML 文件，将标注转换为 YOLO 格式。

    :param annotation_path: VOC XML 文件路径
    :param classes: 类别列表
    :return: 一个包含 YOLO 格式标注的列表
    """
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    size = root.find("size")
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)

    yolo_annotations = []

    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in classes:
            continue
        class_id = classes.index(class_name)

        bbox = obj.find("bndbox")
        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        # 转换为 YOLO 格式
        x_center = ((xmin + xmax) / 2) / img_width
        y_center = ((ymin + ymax) / 2) / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")

    return yolo_annotations


def convert_voc_to_yolo(voc_dir, output_dir, classes, subsets):
    """
    将 VOC 数据集转换为 YOLO 格式。

    :param voc_dir: VOC 数据集解压后的根目录
    :param output_dir: YOLO 格式数据保存目录
    :param classes: VOC 数据集的类别列表
    :param subsets: 子集名称列表，如 ['train', 'val', 'test']
    """
    for subset in subsets:
        subset_file = os.path.join(voc_dir, "ImageSets", "Main", f"{subset}.txt")
        if not os.path.exists(subset_file):
            print(f"Subset file {subset_file} does not exist. Skipping {subset}.")
            continue

        yolo_images_dir = os.path.join(output_dir, subset, "images")
        yolo_labels_dir = os.path.join(output_dir, subset, "labels")
        os.makedirs(yolo_images_dir, exist_ok=True)
        os.makedirs(yolo_labels_dir, exist_ok=True)

        with open(subset_file, "r") as f:
            image_ids = [line.strip() for line in f.readlines()]

        for image_id in image_ids:
            # 图片路径
            src_image_path = os.path.join(voc_dir, "JPEGImages", f"{image_id}.jpg")
            dest_image_path = os.path.join(yolo_images_dir, f"{image_id}.jpg")
            if not os.path.exists(src_image_path):
                print(f"Image {src_image_path} does not exist. Skipping.")
                continue
            shutil.copy(src_image_path, dest_image_path)

            # 标注路径
            annotation_path = os.path.join(voc_dir, "Annotations", f"{image_id}.xml")
            if not os.path.exists(annotation_path):
                print(f"Annotation {annotation_path} does not exist. Skipping.")
                continue

            # 解析并保存 YOLO 格式标注
            yolo_annotations = parse_voc_annotation(annotation_path, classes)
            yolo_label_path = os.path.join(yolo_labels_dir, f"{image_id}.txt")
            with open(yolo_label_path, "w") as label_file:
                label_file.write("\n".join(yolo_annotations))

        print(f"Converted VOC {subset} to YOLO format in {output_dir}/{subset}.")


# VOC 类别列表
VOC_CLASSES = [
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tvmonitor",
]

# 示例调用
SRC_DIR = "/data/DJM/VOC/VOCtar"  # 存放 .tar 文件的目录
EXTRACT_DIR = "/data/DJM/VOC/VOCextracted"  # 解压后的目标目录
OUTPUT_DIR = "/data/DJM/VOC/yolo"  # YOLO 格式数据保存目录
SUBSETS2007 = ["train", "val", "test"]
SUBSETS2012 = ["train", "val"]

# 解压所有 .tar 文件
extract_all_tar_files(SRC_DIR, EXTRACT_DIR)

VOC2012DIR = os.path.join(EXTRACT_DIR, "VOCdevkit", "VOC2012")
VOC2007DIR = os.path.join(EXTRACT_DIR, "VOCdevkit", "VOC2007")


convert_voc_to_yolo(VOC2012DIR, os.path.join(OUTPUT_DIR, "2012"), VOC_CLASSES, SUBSETS2012)

convert_voc_to_yolo(VOC2007DIR, os.path.join(OUTPUT_DIR, "2007"), VOC_CLASSES, SUBSETS2007)
