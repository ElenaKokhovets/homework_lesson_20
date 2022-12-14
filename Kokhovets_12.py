sign = ''
def summ_a():
    a = float(input('Введите первое число а: '))
    b = float(input('Введите второе число b: '))
    return a+b
def raznost_cd():
    c = float(input('Введите первое число c: '))
    d = float(input('Введите второе число d: '))
    return float(c-d)
def delenie():
    n = float(input('Введите первое число n: '))
    m = float(input('Введите второе число m: '))
    try:
        return n/m
    except ZeroDivisionError:
        print('!Делить на ноль нельзя. Введите число m корректно')
def ymnozenie():
    t = float(input('Введите первое число t: '))
    r = float(input('Введите второе число r: '))
    return t*r
print("\033[42m{}\033[0m".format("Что-бы выйти из режима калькулятора вместо знака математической операции введите 0"))
while sign != '0':
    while True:
        print()
        sign = input('Введите знак математической операции из предложенного перечня +-/*:')
        if sign not in '+-/*' and sign != '0':
            print('Введите знак математической операции корректно!')
        else:
            break
    if sign == '+':
        print('Результат сложения a+b :', summ_a())
    elif sign == '-':
        print('Результат вычитания с-d :', raznost_cd())
    elif sign == '/':
        print('Результат деления n/m :', delenie())
    elif sign == '*':
        print('Результат умножения t*r :', ymnozenie())
    elif sign == '0':
        print('Работа калькулятора завершена')