import sys
print("list of arguments: ", sys.argv) # list of arguments that we passed to the program - cписок аругментов что мы
# передали в программу
"""

все параметры, что мы передаем из консоли, находяться в списке argv, a он принадлежит модулю sys, потому мы обязательно 
должны экспортировать этот модуль - библиотеку
самый первый элемент списка - нулевой - это имя нашей программы, тоесть когда мы не работает с аргументами, то у нас 
есть миниму 1 арг - имя программы

all the parameters that we pass from the console are in the argv list, and it belongs to the sys module, so we must 
export this module - a library
the first element of the list - zero - is the name of our program, that is, when we do not work with arguments, then we 
have at least 1 arg - the name of the program

"""
arguments = sys.argv[1:]# slice element 0, that is, from number 1 to the end ([1:]) ( срез, то есть),
# because 0 element is name of file

print(eval(arguments[0]+arguments[1]+arguments[2])) #crooked way1 - don't work without spaces

# normal way
i = 0
argi = '' # empty string
while i < len(sys.argv)-1:
    argi += arguments[i]
    i += 1

#print('args: ' + argi) # our string after string concatenation
print(eval(argi))

#crooked way2 - don't work without spaces
arguments1 = sys.argv[1] # slice element 0, that is, from number 1 to the end ([1:]) ( срез, то есть)
arguments2 = sys.argv[2]
arguments3 = sys.argv[3]
print(eval(arguments1 + arguments2 + arguments3))

"""
eval() - функция для динамического исполнения выражений
Для динамического выполнения кода можно также использовать функцию exec().
Основное различие между eval() и exec() состоит в том, что eval() может выполнять лишь выражения,
тогда как функции exec() можно «скормить» любой фрагмент кода Python.
Если объект кода собран в режиме exec будет возвращено None.

"""