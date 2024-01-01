# c=range(1,4)
# for i in c:
    # print('У Вас 3 попытки. Попытка №',i)
    # number=input('Введите число:')
    # try:
        # int(number)
        # print('Ваше число:',int(number))
    # except ValueError as e:
        # print('Это не число')

# функция map применяет заданную функцию к каждому элементу списка или итерируемого типа. Цикл «спрятан» внутри map.
# from math import sqrt
# l = list(map(sqrt, range(10)))
# print(l) # [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0]

# Возведение в квадрат
# s = int(input('Введите число, которое надо возвести в квадрат:'))
# print(s**2)

# программа по почте пользователя, например, user@myserver.com узнает сервер этой почты
# print('Введите почту, я подскажу её сервер')
# m = input()
# k=0
# while (m[k] != '@'):
    # k=k+1
# index=k+1
# stroka = m[index]
# while (index < len(m)-1):
    # index=index+1
    # stroka = stroka + m[index]
# print(stroka)

# На вход подается некоторая строка. Выведите ее с отступами (количество пробелов, равное позиции строки, начиная с 0).
# stroka=input()
# for i in range(0,len(stroka)):
    # print(i*' '+stroka)

# На вход программе подается строка со словами, разделенными пробелом. 
# Напишите ее так, чтобы каждое слово было с большой буквы. Может использоваться как кириллица, так и латиница.
# s='I want to play GAMES with you HuNNY'
# print(s.title())

# Для входной строки вычислите символ, который встречается в ней чаще всего.
chain="Это входная тестовая строка для подсчета символов"
max = 0
for link in chain:
    if (chain.count(link) > max):
        max = chain.count(link)
        linkMax = link
print(max, linkMax)


# s = input()
# max_count = 0
# max_char = ''
# for i in range(len(s)):
    # if s.count(s[i]) >= max_count:
        # max_count = s.count(s[i])
        # max_char = s[i]
# print(max_char)
