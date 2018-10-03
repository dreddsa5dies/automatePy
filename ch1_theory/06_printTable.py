def maxCounts(tableData):
    # насколько тут все жадно!
    maxCount = []
    maxCountReturns = []
    for i in range(len(tableData)):
        maxCount.append([])
        for y in range(len(tableData[i])):
           maxCount[i].append(len(tableData[i][y]))
    for i in range(len(maxCount)):
        maxCount[i].sort()
        maxCount[i].reverse()
    for i in range(len(maxCount)):
        maxCountReturns.append(maxCount[i][0])
    return maxCountReturns

def printTable(tableData):
    colWidths = maxCounts(tableData)
    strTmp = []
    for y in range(len(tableData[0])):
        strTmp.append([])
        for i in range(len(tableData)): 
            strTmp[y].append(tableData[i][y].rjust(colWidths[i]))
    for i in range(len(strTmp)):
        print(' '.join(strTmp[i]))

tabl = [['apples', 'orages', 'cherries', 'banana'],
            ['Alixe', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
printTable(tabl)