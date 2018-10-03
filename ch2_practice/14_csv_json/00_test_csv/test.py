#! python

import csv

ex = open('example.csv')
exReader = csv.reader(ex)
data = list(exReader)
print(data)
# столбец
for i in range(len(data)):
    print(data[i][1], end=' ')
print()
# строки
for k in range(len(data)):
    for i in range(len(data[0])):
        print(data[k][i], end=' ')
    print()

out = open('out.csv', 'w', newline='')
outWrite = csv.writer(out)
outWrite.writerow(data[0])
out.close()
ex.close()