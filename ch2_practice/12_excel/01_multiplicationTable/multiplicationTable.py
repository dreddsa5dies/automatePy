#! python
# multiplicationTable.py - создание таблиц умножения.

import sys, logging, openpyxl

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Usage
if len(sys.argv) == 1:
    print('Usage: py.exe multiplicationTable.py <int>')

elif len(sys.argv) == 2:
    val = sys.argv[1]
    if val.isdecimal():
        val = int(val)
        logging.info('Введено значение %i' % (val))

        wb = openpyxl.Workbook()
        sheet = wb.get_active_sheet()
        logging.info('Открыта страница книги %s' % (sheet))

        for i in range(1, val+1):
            for y in range(1, val+1):
                sheet.cell(row=i+1, column=1).value = i
                sheet.cell(row=1, column=y+1).value = y
                sheet.cell(row=i+1, column=y+1).value = i*y
        logging.info('Таблица посчитана')

        wb.save(str(val)+'_multiplication.xlsx')
        logging.info('Запись произведена, выход...')
    else:
        logging.info('Введено значение %s' % (val))
        logging.info('Это не номер')
        print('Usage: py.exe multiplicationTable.py <int>')