from random import randint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import datetime
import os

inp = input('Enter text: ')
def transform(strt):
    splitter = list(strt)
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    for i in range(len(splitter)):
        x = randint(0,1)
        if (x == 1):
            if (not splitter[i].isupper()):
                splitter[i] = splitter[i].upper()
    x = "".join(splitter)
    img = Image.open("img/bob.jpg")
    font = ImageFont.truetype("fonts/HelveticaNeueLt.ttf", 20)
    draw = ImageDraw.Draw(img)
    draw.text((20,10), x, (0,0,0), font=font)
    draw = ImageDraw.Draw(img)
    file_name = "out/{}.jpg".format(suffix)
    img.save(file_name)
    img_new = Image.open(file_name)
    img.show()

transform(inp)