#! python

import pyautogui

# пауза в дествиях робота
pyautogui.PAUSE = 1

# мышь резко в левый верхний угол и будет прерывание программы
pyautogui.FAILSAFE = True

# размер экрана
width, height = pyautogui.size()

# перемещение
# for i in range(10):
#     # moveTo - abs position
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# перемещение
# for i in range(10):
#     # moveRel - относительно положения мыши
#     # отрицательные значения - влево вверх
#     pyautogui.moveRel(100, 0, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveTo(0, 100, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveTo(100, 0, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveTo(0, -100, duration=0.25)
#     print(pyautogui.position())

# while True:
#         # Get and print the mouse coordinates.
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         # \b символ забоя - очищает экран
#         print('\b' * len(positionStr), end='', flush=True)

# # клик левой клавиши в районе 10.5
# pyautogui.click(10, 5)

# dragTo - перетаскивание окна на позицию
# dragRel - перетаскивание окна в позицию относительно мыши