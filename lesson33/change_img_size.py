from PIL import Image
import os

def generate_thumbnail(image_path, thumbnail_size=(100, 100)):
    """
    Генерирует превью изображения размером 100x100 пикселей.

    :param image_path: Путь к файлу изображения.
    :param thumbnail_size: Размер превью изображения, по умолчанию (100, 100).
    """
    # Открываем изображение
    with Image.open(image_path) as img:
        # Создаем превью
        img.thumbnail(thumbnail_size)
        
        # Генерируем новое имя файла для превью
        base, ext = os.path.splitext(image_path)
        thumbnail_path = f"{base}_thumbnail{ext}"
        
        # Сохраняем превью
        img.save(thumbnail_path, "JPEG")
        
        print(f"Thumbnail saved at: {thumbnail_path}")

# Пример использования
generate_thumbnail("path/to/your/image.jpg")
