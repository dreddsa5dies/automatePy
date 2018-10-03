#! python
# strongPass.py - функция проверки пароля.

import re

def checkPass(prompt):
    # Сильным будет пароль не меньше 8 символов, в вернем и нихнем регистре и 1 цифра
    # passRe = re.compile(r'(([0-9a-zA-Z]){8,})')
    passRe = re.compile(r'([0-9a-zA-Z]){8,}')
    passReDit = re.compile(r'.*(\d)+.*')
    if passRe.match(prompt) and passReDit.match(prompt):
        print('Pass ok')
    else:
        print('Bad pass')

checkPass('Password')
checkPass('Password12')
checkPass('12345678')
checkPass('Admin')
checkPass('Qwerty1234')