from PIL import Image

def compress_jpg_image(input_path, output_path, quality=85):
    # 打开图片
    img = Image.open(input_path)

    # 保存图片时，指定质量参数并启用优化模式
    img.save(output_path, "JPEG", quality=quality, optimize=True)

