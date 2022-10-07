# imports
import PIL
from PIL import Image

# open image with python image library
img = PIL.Image.open('FireExample.jpg')
pix = img.load()

# open file to write seed to
f = open("seed_output.txt", "w")

# loop through image pixels, counting ones represented by fire
for i in range(1920):
    for j in range(1080):
        f.write(str(pix[i, j]))

# close file
f.close()
