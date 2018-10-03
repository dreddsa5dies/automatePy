#! python

import os
from PIL import ImageFont, Image, ImageDraw

im = Image.new('RGBA', (200, 200), 'white')

draw = ImageDraw.Draw(im)

draw.text((20, 150), 'Hello', fill='black')

fontsFolder = 'FONT_FOLDER'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'FFFFFF', fill='gray', font=arialFont)

im.save('text.png')