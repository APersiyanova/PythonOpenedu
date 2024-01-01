# Сумма цифр числа 498578324323 равна 58. У 58 сумма цифр — 13, а у 13 — 4. 
# На вход подается строка, содержащая число, которое "Сократщается" указанным образом до 1 цифры.
# Формат ввода
# 498578324323
# Формат вывода
# 4

number = list(input())
# print(number)
while (len(number)>1):
    digit = 0
    for current_digit in number:
        digit=digit+int(current_digit)
        # print(digit)
    number = [int(d) for d in str(digit)]
    # print(number)
result=map(str,number)
result = ''.join(result) 
result=int(result)
print(result)
