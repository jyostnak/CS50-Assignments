import sys
from  PIL import Image, ImageOps

if len(sys.argv) <3:
    sys.exit("Too few command-line argument")

if len(sys.argv) > 3:
    sys.exit("Too many command=line arguments")

input_name = sys.argv[1]
output_name = sys.argv[2]

valid = (".jpg", ".jpeg", ".png")

if not input_name.endswith(valid) or not output_name.endswith(valid):
    sys.exit("Invalid input")

ext1 = input_name.split(".")[-1]
ext2 = output_name.split(".")[-1]

if ext1 != ext2:
    sys.exit("Input and output have different extensions")
try:
    shirt = Image.open("shirt.png")
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
size = shirt.size
fitted = ImageOps.fit(input_image, size)
fitted.paste(shirt, shirt)
fitted.save(sys.argv[2])


