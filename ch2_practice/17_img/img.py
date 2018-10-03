#! python

from PIL import Image, ImageColor

#  открытие файла изображения и его параметры
catIm = Image.open('zophie.png')
print(catIm.size)
print(catIm.filename)
print(catIm.format)

# пересохранение в JPG
catIm.save('z.jpg')

# новое изображение
im = Image.new('RGBA', (100, 100), 'red')
im.save('new.png')

# обрезка
croppedIm = catIm.crop((335,345,565,560))
croppedIm.save('cropped.png')

# copy paste rotate resize
catCopy = catIm.copy()
catCopy.paste(croppedIm.rotate(180), (335,345))
catCopy.save('pasted.png')
widthCropp, heightCropp = croppedIm.size
catCopy = catCopy.resize((int(widthCropp/3), int(heightCropp/3)))
catCopy.save('pasted_resized.png')
# rotate на 6%
croppedIm.rotate(6, expand=True).save('rotate6.png')
# зеркально
croppedIm.transpose(Image.FLIP_TOP_BOTTOM).save('TOP.png')
croppedIm.transpose(Image.FLIP_LEFT_RIGHT).save('LEFT.png')
# отдельные пиксели
width, height = croppedIm.size
for i in range (int(width/2)):
    for y in range(int(height/2)):
        croppedIm.putpixel((i, y), ImageColor.getcolor('darkgrey', 'RGBA'))
croppedIm.save('putpixel.png')
