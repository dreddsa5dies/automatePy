#! python

from PIL import ImageColor

# белый     (255, 255, 255, 255)
# зеленый   (0, 128, 0, 255)
# серый     (128, 128, 128, 255)
# черный    (0, 0, 0, 255)
# красный   (255, 0, 0, 255)
# синий     (0, 0, 255, 255)
# желтый    (255, 255, 0, 255)
# пурпурный (128, 0, 128, 255)

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getrgb('red'))