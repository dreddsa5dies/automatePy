#! python

import pyautogui, time

time.sleep(5)

pyautogui.click()

dist = 200

while dist > 0 :
    pyautogui.dragRel(dist, 0, duration=0.2) #сдвиг вправо
    dist = dist - 5
    pyautogui.dragRel(0, dist, duration=0.2)
    pyautogui.dragRel(-dist, 0, duration=0.2)
    dist = dist - 5
    pyautogui.dragRel(0, -dist, duration=0.2)