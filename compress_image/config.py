import logging

# 配置日志记录
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

# 设置上传和保存路径
UPLOAD_ORIGIN_JPG = 'uploads/jpeg'
UPLOAD_CONVERTED_JPG = 'result/converted/jpeg'
COMPRESSED_JPG_FOLDER = 'result/compressed/jpeg'