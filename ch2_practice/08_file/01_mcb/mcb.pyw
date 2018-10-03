#! python
# mcb.pyw - сохраняет и загружает фрагменты текста в буфер обмена.
# Использование:    py.exe mcb.pyw save <keyword> - сохраняет буфер обмена по ключу keyword.
#                   py.exe mcb.pyw <keyword> - загружает ключевое слово в буфер обмена.
#                   py.exe mcb.pyw list - загружает все слова в буфер обмена.
#                   py.exe mcb.pyw delete <keyword> - удаляет данные по ключу keyword.
#                   py.exe mcb.pyw delete - удаляет все данные по ключу keyword.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 1:
    print('''Использование:    py.exe mcb.pyw save <keyword> - сохраняет буфер обмена по ключу keyword.
                  py.exe mcb.pyw <keyword> - загружает ключевое слово в буфер обмена.
                  py.exe mcb.pyw list - загружает все слова в буфер обмена.
                  py.exe mcb.pyw delete <keyword> - удаляет данные по ключу keyword.
                  py.exe mcb.pyw delete - удаляет все данные.''')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        print('All saves: %s' % str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
