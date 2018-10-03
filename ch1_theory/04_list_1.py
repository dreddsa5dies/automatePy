def printList(val):
    for k in range(len(val)):
        if k != len(val)-1 and k != len(val)-2:
            print(val[k], end=', ')
        elif k == len(val)-2:
            print(val[k], end=' and ')
        else:
            print(val[k])

spam = ['app', 'ban', 'tof', 'cat']
printList(spam)
vl = str(input('Введите строку: '))
lis = vl.split(" ")
printList(lis)