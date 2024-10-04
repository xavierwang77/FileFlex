import os
from tqdm import tqdm
from .functions import compress_jpg_image
from .config import UPLOAD_ORIGIN_JPG, UPLOAD_CONVERTED_JPG, COMPRESSED_JPG_FOLDER, logging

def run(handle_converted: bool) -> None:
    # 检查目标路径是否存在
    if not os.path.exists(UPLOAD_ORIGIN_JPG):
        logging.error(f"The folder {UPLOAD_ORIGIN_JPG} does not exist.")
        raise FileNotFoundError(f"The folder {UPLOAD_ORIGIN_JPG} does not exist.")
    if not os.path.exists(UPLOAD_CONVERTED_JPG):
        logging.error(f"The folder {UPLOAD_CONVERTED_JPG} does not exist.")
        raise FileNotFoundError(f"The folder {UPLOAD_CONVERTED_JPG} does not exist.")
    if not os.path.exists(COMPRESSED_JPG_FOLDER):
        logging.error(f"The folder {COMPRESSED_JPG_FOLDER} does not exist.")
        raise FileNotFoundError(f"The folder {COMPRESSED_JPG_FOLDER} does not exist.")

    # 检查传入参数类型
    if not isinstance(handle_converted, bool):
        logging.error(f"The param handleConverted is not bool type")
        raise TypeError(f"The param handleConverted is not bool type")

    # 选择数据源
    if not handle_converted:
        source_folder = UPLOAD_ORIGIN_JPG
        logging.info(f"Handling files from {UPLOAD_ORIGIN_JPG}")
    else:
        source_folder = UPLOAD_CONVERTED_JPG
        logging.info(f"Handling files from {UPLOAD_CONVERTED_JPG}")

    # 检查目标路径是否为空
    if not os.listdir(source_folder):
        logging.info(f"The folder {source_folder} is empty.")
        return

    # 遍历源文件夹并获取所有 jpg/jpeg 文件
    files_to_process = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(COMPRESSED_JPG_FOLDER, file.replace('.jpeg', '.jpg'))
                files_to_process.append((input_path, output_path))

    # 使用 tqdm 添加进度条
    for input_path, output_path in tqdm(files_to_process, desc="Compressing images", unit="file"):
        try:
            compress_jpg_image(input_path, output_path)
        except Exception as e:
            logging.error(f"Failed to convert {input_path}: {e}")

    logging.info("All jpeg images have been compressed successfully.")
