#! python
# reSearch.py - читает файлы в каталоге и ищет нужный текст.
# Использование:    py.exe reSearch.py <dist> - считывает все файлы в папке dist и ищет строки по указанной регулярке

import sys, re, os

# Usage
if len(sys.argv) == 1:
    print('''Использование:    py.exe reSearch.py <dist>''')
# Oen file
elif len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        reStr = input('Введите регулярное выражение: ')
        reComp = re.compile(reStr)
        count = 0
        for file in os.listdir(path):
            if not os.path.isdir(file) and str(file).lower().endswith('txt'):
                count = count + 1
                tmp = open(file)
                allFinds = reComp.findall(tmp.read())
                if len(allFinds) == 0:
                    print('Не найдено')
                else:
                    for v in allFinds:
                        print(v)
                tmp.close()
        if count == 0:
            print('TXT файлы не найдены')
    else:
        print('Это не директория для поиска!')
    