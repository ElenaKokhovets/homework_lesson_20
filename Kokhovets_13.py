#ДЗ на понедельник:
# 1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0
#2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой


a1 = [1,2,3,'a','bc8?']
a2 = (1,2,3,'a','bc8?',7,8,9)
a3 = 77988
a4 = '788dfgh'
def decorator(function):
    def wrapper(arg):
        print('Старт функции: ', str(function.__name__),
              'Тип данных, отправленный в функцию: ', str(type(arg)))
        return function(arg)
    return wrapper
@decorator
def spisok(a1):
    k1=0
    k2=0
    a1_1=str(a1)
    for i in a1_1:
        if i.isalpha():
            k1 += 1
        if i.isdigit():
            k2 += 1
    return 'В списке колличество букв', k1,'цифр', k2
@decorator
def kortez(a2):
    m = []
    for i in a2:
        if type(i) == str:
            m.append(i)
    len_k = len(''.join(m))
    return len_k
@decorator
def chislo(a3):
    a3_1 = list(str(a3))
    t = 0
    for i in a3_1:
        if int(i) % 2 != 0:
            t += 1
    return t
@decorator
def stroka (a4):
    a4_1 = list(a4)
    s = 0
    for i in a4_1:
        if i.isalpha():
            s += 1
    return s
if type (a1) == list: print(*spisok(a1))
if type (a2) == tuple: print('Длина всех строк кортежа:',kortez(a2))
if type (a3) == int: print('Количествово нечётных цифр в числе:',chislo(a3))
if type (a4) == str: print('Количествово букв в строке:',stroka(a4))








