#! python
# excelSpreadsheets.py - перевод Excel в CSV.

import csv, openpyxl, os, sys

def excelSpreadsheets(dst):
    # все что есть в директории
    for excelFile in os.listdir(dst):
        # но не папки
        if os.path.isdir(excelFile):
            continue
        else:
            # и никакие файлы кроме XLSX
            if str(excelFile).endswith('.xlsx'):
                wb = openpyxl.load_workbook(excelFile)
                # все страницы - отдельный файл
                for sheetName in wb.get_sheet_names():
                    sheet = wb.get_sheet_by_name(sheetName)
                    out = open(sheetName + '.csv', 'w', newline='')
                    outWrite = csv.writer(out)
                    # проход построчно
                    for rowNum in range(1, sheet.get_highest_row() + 1):
                        rowData = []
                        for colNum in range(1, sheet.get_highest_column()+ 1):
                            rowData.append(sheet.cell(row=rowNum, column=colNum).value)
                        outWrite.writerow(rowData)
                    out.close()

# Usage
if len(sys.argv) == 1:
    print('Usage: py.exe excelSpreadsheets.py <dst>')

elif len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        excelSpreadsheets(sys.argv[1])
    else:
        print('Это не директория для поиска!')
        print('Usage: py.exe excelSpreadsheets.py <dist>')