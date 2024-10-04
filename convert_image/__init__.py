import os
from .config import UPLOAD_HEIC_FOLDER, UPLOAD_JPEG_FOLDER, CONVERTED_JPEG_FOLDER
from .run import run

# 初始化目录
os.makedirs(UPLOAD_HEIC_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_JPEG_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_JPEG_FOLDER, exist_ok=True)

__all__ = [
    'run'
]
