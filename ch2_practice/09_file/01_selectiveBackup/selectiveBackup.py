#! python
# selectiveBackup.py - обход дерева каталогов и копирования спец файлов в новый каталог.
# Использование:    py.exe selectiveBackup.py <dist>

import sys, os, shutil

def search(dist, endsFile, dst):
    count = 0
    for folderName, subFolders, filenames in os.walk(dist):
        print('Копирование файлов из папки %s' % (folderName))
        # файлы
        for filename in filenames:
            if filename.endswith(endsFile):
                count = count + 1
                print('Сохранение в %s' % (shutil.copy(os.path.join(folderName, filename), os.path.join(dst, filename))))
    if count == 0:
        print('Не найдено ничего')

# Usage
if len(sys.argv) == 1:
    print('Usage: py.exe selectiveBackup.py <dist>')
# Open dist
elif len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        howSearch = str(input('Кого ищем? '))
        # корректный ввод директории для сохранения
        while True:
            howSave = str(input('Куда сохраним? '))
            if os.path.isdir(howSave):
                break
            else:
                print('Нужна рабочая директория!')

        search(sys.argv[1], howSearch, howSave)
    else:
        print('Это не директория для поиска!')
        print('Usage: py.exe selectiveBackup.py <dist>')