#! python

import time, threading

print('Start')

def tekeANap():
    time.sleep(5)
    print('Weekup!')

threadAll = []

# вызов отдельного треда
threadObj = threading.Thread(target=tekeANap)
threadAll.append(threadObj)
threadObj.start()

# передача аргументов в функци в отдельном треде
threadObject = threading.Thread(target=print, args=['Solo', 'Viktor', 'dreddsa5dies'], kwargs={'sep': ' & '})
threadAll.append(threadObject)
threadObject.start()

# ожидание выполнения
for thr in threadAll:
    thr.join()

print('End')