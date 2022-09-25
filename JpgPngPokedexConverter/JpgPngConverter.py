import sys
import os
from PIL import Image

# Grab 1st and 2nd arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if new folder exists, if not create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through Pokedex and convert to PNG and save to new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clear_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clear_name}.png', 'png')
    print('Images saved')
