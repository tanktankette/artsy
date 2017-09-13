from random import random
from PIL import Image
from PIL import ImageDraw

size_x = 1000
size_y = 1000


def generateField(num):
    field = []
    for star in range(num):
        field.append((random() * size_x, random() * size_y, random()))
    return field


img = Image.new('RGB', (size_x, size_y))
draw = ImageDraw.Draw(img)

for star in generateField(200):
    point_1 = (star[0], star[1] - 2)
    point_2 = (star[0] - 2, star[1] + 2)
    point_3 = (star[0] + 2, star[1] + 2)
    draw.polygon([point_1, point_2, point_3], fill=(255, 255, 255))

img.show()
