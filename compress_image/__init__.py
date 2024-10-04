import os
from .config import UPLOAD_ORIGIN_JPG, UPLOAD_CONVERTED_JPG, COMPRESSED_JPG_FOLDER
from .run import run

# 初始化目录
os.makedirs(UPLOAD_ORIGIN_JPG, exist_ok=True)
os.makedirs(UPLOAD_CONVERTED_JPG, exist_ok=True)
os.makedirs(COMPRESSED_JPG_FOLDER, exist_ok=True)

__all__ = [
    'run'
]