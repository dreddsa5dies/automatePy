#! python
# xlsx2txt.py - вставка данных из excel в TXT.

import openpyxl, sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print('Usage: py.exe txt2xlsx.py <file>')

elif len(sys.argv) == 2:
	# проверка вх данных
	fileName = sys.argv[1]
	if fileName.endswith('.xlsx'):
		wb = openpyxl.load_workbook(fileName)
		sheet = wb.get_active_sheet()
		maxCol = sheet.get_highest_column()
		
		columnData = []
		for col in range(maxCol):
			columnData.append(sheet.columns[col])
		
		for data in range(len(columnData)):
			tmpFile = open(str(data) + ".txt", "w")
			for obj in range(len(columnData[data])):
				if columnData[data][obj].value != None:
					tmpFile.writelines(columnData[data][obj].value)
			tmpFile.close()