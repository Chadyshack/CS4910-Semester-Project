import PIL
from PIL import Image

img = PIL.Image.open('FireExample.jpg')
pix = img.load()

for i in range(192):
    for j in range(108):
        print(pix[i, j][0])
