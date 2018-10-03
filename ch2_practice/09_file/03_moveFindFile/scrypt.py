#! python
# scrypt.py - поиск пропусков в нумерации файлов.
# Использование:    py.exe scrypt.py <dist>

import sys, os, shutil, re

def search(dist):
    # форма поиска
    reFile = re.compile(r'(\d){3}')
    # хранилище результатов
    allFinds = {}
    # все файлы и папки
    value = os.listdir(dist)
    path = os.path.abspath(dist)
    # файлы
    for val in value:
        # нужны только файлы,не папки
        if os.path.isdir(val):
            continue
        else:
            if reFile.search(val) != None:
                mo = reFile.search(val)
                allFinds[int(mo.group())] = os.path.join(path,val)
  
    # отчет
    if len(allFinds)!=0:
        # перемещение
        tmp = 1
        for v in allFinds:
            # если по порядку то пропуск
            if tmp == v:
                tmp = tmp+1
                continue
            else:
                print('перемещаю %s' % (allFinds[v]))
                # подбор имени
                # расскоментировать для перемещения
                if tmp < 10:
                    fileName = 'spam00' + str(tmp) + '.txt'
                    print(os.path.join(path, fileName))
                    # shutil.move(allFinds[v], os.path.join(path, fileName))
                elif tmp < 100:
                    fileName = 'spam0' + str(tmp) + '.txt'
                    print(os.path.join(path, fileName))
                    # shutil.move(allFinds[v], os.path.join(path, fileName))
                elif tmp < 1000:
                    fileName = 'spam' + str(tmp) + '.txt'
                    print(os.path.join(path, fileName))
                    # shutil.move(allFinds[v], os.path.join(path, fileName))
                tmp = tmp+1
    else:
        print('Файлы не перемещались...')

# Usage
usage = 'Usage: py.exe scrypt.py <dist>'
if len(sys.argv) == 1:
    print(usage)
# Open dist
elif len(sys.argv) == 2:
    dist = sys.argv[1]
    if os.path.isdir(dist):
        search(dist)
    else:
        print('Это не директория для поиска!')
        print(usage)