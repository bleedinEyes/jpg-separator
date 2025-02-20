import os
from PIL import Image

source_dir = 'resources/source_img/'
left_output_dir = 'resources/output_img/left/'
right_output_dir = 'resources/output_img/right/'

os.makedirs(left_output_dir, exist_ok=True)
os.makedirs(right_output_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(source_dir, filename)
        image = Image.open(image_path)

        width, height = image.size

        if width != 3200 or height != 1200:
            print(f"Изображение {filename} не имеет размер 3200x1200. Пропускаю...")
            continue

        left_image = image.crop((0, 0, width // 2, height))
        right_image = image.crop((width // 2, 0, width, height))

        base_name = os.path.splitext(filename)[0]
        left_image_name = f"{base_name}_left.jpg"
        right_image_name = f"{base_name}_right.jpg"

        left_image.save(os.path.join(left_output_dir, left_image_name))
        right_image.save(os.path.join(right_output_dir, right_image_name))

        print(f"Изображение {filename} успешно разделено на два файла: {left_image_name} и {right_image_name}")