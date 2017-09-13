from random import random
from PIL import Image
from PIL import ImageDraw

size_x = 2000
size_y = 6000


def generateField(num):
    field = []
    for star in range(num):
        field.append((random(), random(), random(), random()))
    return field


img = Image.new('RGBA', (size_x, size_y), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

for star in generateField(1000):
    x, y = star[0] * size_x, star[1] * size_y
    brightness = int(star[2] * 100 + star[1] * 150)
    star_size = star[3] + 1

    if random() >= .5:
        point_1 = (x, y - star_size)
        point_2 = (x - star_size, y + star_size)
        point_3 = (x + star_size, y + star_size)
    else:
        point_1 = (x, y + star_size)
        point_2 = (x - star_size, y - star_size)
        point_3 = (x + star_size, y - star_size)

    draw.polygon([point_1, point_2, point_3], fill=(255, 255, 255, brightness))

img.save('test.png')
