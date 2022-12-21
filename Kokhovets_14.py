#ДЗ на четверг:
# Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
# Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.
# Петя -> 'Привет, ПЕТЯ'
#
# Найти сумму цифр числа с помощью рекурсии. 112 = 4
print('Task №1')
def decorator(function):
    def wrapper(arg):
        arg=arg.upper()
        return function(arg)
    return wrapper

name1 = input('Введите имя: ')

@decorator
def name (N):
    return N
print('Привет,', name(name1))

# Task №2
# Найти сумму цифр числа с помощью рекурсии. 112 = 4

print()
print('Task №2 (методом рекурсии)')
chislo = input('Введите число: ')
chislo = list(chislo)
chislo_s=[]
for i in chislo:
    chislo_s.append(int(i))
def summa_s(a):
    if len(a) != 0:
        return a[0]+summa_s(a[1:])
    else: return 0
print('Сумма цифр числа :', summa_s(chislo_s))

print()
print('Task №2 (не методом рекурсии)')
def summa():
    chislo = input('Введите число: ')
    if len(chislo)!=0:
        s=0
        for i in chislo:
            s +=int(i)
    return s
print('Сумма цифр числа :', summa())