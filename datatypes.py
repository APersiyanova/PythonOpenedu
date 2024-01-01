s = 'пиШу каК Хочу, тО сТроЧнымИ букаМИ, то зАглАвными'
print(s)
sl=s.lower()
print(sl+ ', а потом исправляю на строчные')
print('А могу и конвертировать заглавные в строчные, а строчные в заклавные: '+s.swapcase())
# Классы, у которых вызываются конструкторы, создающие:
c = 3+int("456")
print(c) # число из строки. ЧИСЛА И СТРОКИ - НЕЗАВИСИМЫЕ ТИПЫ ДАННЫХ, они не изменяются
l = "My favourite number is "+str(c)
print(l) # строку из числа
print(bool(2)) # логический тип
print(float(45)) #вещественное число
li=list(l)
print(li) # список ['M', 'y', ' ', 'f', 'a', 'v', 'o', 'u', 'r', 'i', 't', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', 'i', 's', ' ', '4', '5', '9']
print(True+True)
# Строки символов (НЕИЗМЕНЯЕМЫЕ) и списки произвольных элементов- это контейнеры, по данным которых можно пробежаться
li[1]=li[-2]
print(li[1],li[-1],' ',s[1],s[-1]) # y 'и'
print(s[::-1]) # Инвертировать строку
liShort = ['A','a',0,'F','f',6]
print(liShort)
liShort.append(17)
print(liShort)
liShort.insert(3,'E')
print(liShort)
liShort.pop()
print(liShort)
liShort.pop()
print(liShort)
liShort.pop(1)
print(liShort)
print(liShort[1],liShort[2],sep="*!*")