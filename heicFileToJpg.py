from PIL import Image
from pillow_heif import register_heif_opener
import os
# Doc : https://safjan.com/convert-heic-and-heif-to-jpg-png-bmp-with-python/#:~:text=Use%20Pillow,-Step%201%3A%20Installing&text=We%20then%20use%20the%20open,image%20as%20a%20JPEG%20file.

register_heif_opener()

# Image Directory
directory = "Images"

# Open the image files : Get list of HEIF and HEIC files in director
files = [f for f in os.listdir(directory) if f.endswith('.HEIC') or f.endswith('.heif')]

# Convert each file to JPEG
for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))