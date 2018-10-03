#! python

import time, datetime

# отсчет времени
startTime = time.time()
time.sleep(1)
print(time.time())
time.sleep(1)
endTime = time.time()
print('Время %s ' % (endTime - startTime))

# сейчас
dateNow = datetime.datetime.now()
print(dateNow.year)
print(dateNow.hour)
print(dateNow.second)

# дату в строку
print(datetime.datetime.fromtimestamp(time.time()).isocalendar()[0])
print(dateNow.strftime('%d "%B" %Y %H:%M:%S'))

# из строки в дату
strDate = '21.01.2018'
dateNow2 = datetime.datetime.strptime(strDate, '%d.%m.%Y')
print(dateNow2.strftime('%d "%B" %Y %H:%M:%S'))