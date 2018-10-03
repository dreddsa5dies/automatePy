def collatz(number):
    if number%2==0:
        return number//2
    else:
        return number*3+1

# Проверка введенного значения (без try/exept)
def interNum():
    while True:
        print('Введите целое число:')
        prompt = input()
        if prompt.isdecimal():
            return int(prompt)
            break
        print('Требуется ввод целого числа')

num = interNum()
allNum = []
while True:
    num = collatz(num)
    allNum.append(num)
    if num == 1:
        break
    else:
        continue

for i in allNum:
    print(i, end=" ")

print()

allNum.sort(reverse=True)

for i in allNum:
     print(i, end=" ")

# allNum = sorted(allNum)
# #  reverse sort list
# for i in range(len(allNum)):
#     # not out of range i+1
#     print(allNum[len(allNum)-(i+1)], end=" ")