# config.py

import logging

# 配置日志记录
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

# 设置上传及生成文件的保存路径
UPLOAD_HEIC_FOLDER = 'uploads/heic'  # 上传文件保存路径
UPLOAD_JPEG_FOLDER = 'uploads/jpeg'  # 上传文件保存路径
CONVERTED_JPEG_FOLDER = 'result/converted/jpeg'  # 转换后的文件保存路径

