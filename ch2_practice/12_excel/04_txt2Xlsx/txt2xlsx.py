#! python
# txt2xlsx.py - вставка данных из TXT в excel.

import openpyxl, sys, os

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print('Usage: py.exe txt2xlsx.py <dist>')

elif len(sys.argv) == 2:
	# проверка вх данных
	if os.path.isdir(sys.argv[1]):
		allFiles = os.listdir(sys.argv[1])

		allFilesTxt = []
		for v in allFiles:
			if str(v).endswith('txt'):
				allFilesTxt.append(v)

		wb = openpyxl.Workbook()
		sheet = wb.get_active_sheet()

		for k in range(len(allFilesTxt)):
			file = open(allFilesTxt[k])
			dataTxt = file.readlines()
			for d in range(len(dataTxt)):
				sheet.cell(row=d+1, column=k+1).value = dataTxt[d]
		
		wb.save('txt_table.xlsx')