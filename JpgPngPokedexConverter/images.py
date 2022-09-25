from ctypes import resize
from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

# Add filter over image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

# Convert image and open it
filtered_img = img.convert('L')
filtered_img.save("convert.png", "png")
filtered_img.show()

# Rotate image
crooked = filtered_img.rotate(90)
crooked.save("crooked.png", "png")

# Rotate image
resize = filtered_img.resize((300, 300))
resize.save("rotate.png", "png")

# Crop image
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("crop.png", "png")

# Resize image
img.thumbnail((400, 200))
img.save("thumbnail.png", "png")