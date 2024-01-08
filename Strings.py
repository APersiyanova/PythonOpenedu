# Строка - упорядоченная последовательность символов
# dir(str)         Посмотреть все доступные методы для строк
# help(str.find)   Получить информацию о доступном методе, напр., find
name = input('Your name: ')
sername = input('Your sername: ')
if (len(name)>1 and len(sername)>1):
    print('Hello, {0}{1} {2}{3}! {4}'.format(name[0].upper(),ord(name[1]),sername[0].upper(),ord(sername[1]),'Nice to meet you!'))
print(chr(65)) # A
print(chr(97)) # a
print(chr(66)) # B
if (name.find('n') != -1):
    print(name.find('n'))
    print(name.lower().count('n'))
if 'nn' in name:
    name.replace('nn','n')
print(name)
print(name.replace('nn','n'))
s ='Hello_World!'[7:4:-1]
print(s) # 'oW_'    начиная с 6 по 5 (предыдущую относительно 4), в обратном порядке
ss ='Hello, \'World!\''+ '\t I come to conquer you'
print(ss)
print(r'Hello, \'World!\''+ r'\t I come to conquer you') # raw string