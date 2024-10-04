import os
from PIL import Image
import pyheif
from .config import logging

# 将HEIC文件转换为JPEG
def heic_to_jpeg(heic_path, jpeg_path):
    # 检查参数
    if not os.path.exists(heic_path):
        logging.error(f"File not found: {heic_path}")
        raise FileNotFoundError(f"File not found: {heic_path}")
    if not heic_path.lower().endswith('.heic'):
        logging.error("The file is not a HEIC file.")
        raise ValueError("The file is not a HEIC file.")
    if not jpeg_path.lower().endswith('.jpg'):
        logging.error("The target file path not end with .jpg.")
        raise ValueError("The target file is not a JPEG file.")

    # 使用pyheif读取HEIC文件
    heif_file = pyheif.read(heic_path)

    # 将heif数据转换为PIL支持的格式
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride
    )

    # 保存为JPEG格式
    image.save(jpeg_path, "JPEG")

