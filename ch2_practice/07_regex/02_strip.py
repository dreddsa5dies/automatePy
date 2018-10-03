#! python
# strip.py - функция strip by regexp.

import re

def stripStr(prompt, sub=None):
    if sub == None:
        strRe1 = re.compile('^(\s)')
        strRe2 = re.compile('(\s)$')
        prompt = strRe1.sub('', prompt)
        prompt = strRe2.sub('', prompt)
    else:
        strRe = re.compile(sub)
        prompt = strRe.sub('', prompt)
    
    return prompt

print(' Строка 111 '.strip())
print(stripStr(' Строка 111 '))
print(stripStr(' Строка 111 ', '1'))