#! python
# getSize.py - обход дерева каталогов и поиск больших файлов.
# Использование:    py.exe getSize.py <dist>

import sys, os, shutil

def search(dist):
    allFinds = []
    for folderName, subFolders, filenames in os.walk(dist):
        # файлы
        for filename in filenames:
            if os.path.getsize(os.path.join(folderName, filename)) > 104857600:
                allFinds.append(os.path.join(folderName, filename))
    if len(allFinds)!=0:
        print('Найдены: ')
        for v in allFinds:
            print('%s %i MB' % (v, int(os.path.getsize(v)/1048576)))
    else:
        print('Файлы больше 100 MB не найдены')

# Usage
if len(sys.argv) == 1:
    print('Usage: py.exe getSize.py <dist>')
# Open dist
elif len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        search(sys.argv[1])
    else:
        print('Это не директория для поиска!')
        print('Usage: py.exe getSize.py <dist>')