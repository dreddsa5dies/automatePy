#! python
# madLibs.py - читает файлы и меняет нужный текст.
# Использование:    py.exe mcb.py <file> - считывает file и меняет Прилагательные, существительные и т.д.

import sys, re

# Usage
if len(sys.argv) == 1:
    print('''Использование:    py.exe mcb.py <file>''')
# Oen file
elif len(sys.argv) == 2:
    # read file
    openFile = open(sys.argv[1])
    # get strline & strip this
    content = openFile.read()
    strLine = str(content).split()
    # if strline[] == ADJ NONE OR VERB - get answer from users
    finalStr = ''
    checkAdj = re.compile(r'ADJECTIVE')
    checkNoun = re.compile(r'NOUN')
    checkVerb = re.compile(r'VERB')
    for i in range(len(strLine)):
        tmpVal = ''
        if checkAdj.match(strLine[i]):
            tmpStr = checkAdj.sub(input('Введите имя прилагательное: '), strLine[i])
            finalStr = finalStr + " " + tmpStr
        elif checkNoun.match(strLine[i]):
            tmpStr = checkNoun.sub(input('Введите имя прилагательное: '), strLine[i])
            finalStr = finalStr + " " + tmpStr
        elif checkVerb.match(strLine[i]):
            tmpStr = checkVerb.sub(input('Введите имя прилагательное: '), strLine[i])
            finalStr = finalStr + " " + tmpStr
        else:
            finalStr = finalStr + " " + strLine[i]
    openFile.close()
    fileName = sys.argv[1] + '_tmp.txt'
    saveFile = open(fileName, 'w')
    saveFile.write(finalStr)
    saveFile.close()