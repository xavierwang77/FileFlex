import os
from tqdm import tqdm
from .functions import heic_to_jpeg
from .config import UPLOAD_HEIC_FOLDER, UPLOAD_JPEG_FOLDER, CONVERTED_JPEG_FOLDER, logging

def run() -> None:
    # 检查目标路径是否存在
    if not os.path.exists(UPLOAD_HEIC_FOLDER):
        logging.error(f"The folder {UPLOAD_HEIC_FOLDER} does not exist.")
        raise FileNotFoundError(f"The folder {UPLOAD_HEIC_FOLDER} does not exist.")
    if not os.path.exists(UPLOAD_JPEG_FOLDER):
        logging.error(f"The folder {UPLOAD_JPEG_FOLDER} does not exist.")
        raise FileNotFoundError(f"The folder {UPLOAD_JPEG_FOLDER} does not exist.")
    if not os.path.exists(CONVERTED_JPEG_FOLDER):
        logging.error(f"The folder {CONVERTED_JPEG_FOLDER} does not exist.")
        raise FileNotFoundError(f"The folder {CONVERTED_JPEG_FOLDER} does not exist.")

    # 检查目标路径是否为空
    if not os.listdir(UPLOAD_HEIC_FOLDER):
        logging.info(f"The folder {UPLOAD_HEIC_FOLDER} is empty.")
        return

    # 收集所有的 HEIC 文件路径
    heic_files = []
    for root, dirs, files in os.walk(UPLOAD_HEIC_FOLDER):
        for file in files:
            if file.endswith('.HEIC') or file.endswith('.heic'):
                heic_path = os.path.join(root, file)
                jpeg_path = os.path.join(CONVERTED_JPEG_FOLDER, file.replace('.HEIC', '.jpg').replace('.heic', '.jpg'))
                heic_files.append((heic_path, jpeg_path))

    # 使用 tqdm 添加进度条来处理文件
    for heic_path, jpeg_path in tqdm(heic_files, desc="Converting HEIC to JPEG", unit="file"):
        try:
            heic_to_jpeg(heic_path, jpeg_path)
        except Exception as e:
            logging.error(f"Failed to convert {heic_path}: {e}")

    logging.info("All HEIC files have been converted to JPEG format.")
