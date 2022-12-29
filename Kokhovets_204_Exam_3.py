#1. Напишите функцию, которая запрашивает у пользователя номер карты,
# CVC-код и PIN-код. После этого выводит на экран номер карты с первыми четырьмя цифрами,
# остальные заменены на звездочки, CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

print ("Task №1 :")
def сard(сard_number, CVC, PIN):
    print('Номер карты: ', сard_number[0:4]+'*'*(len(сard_number)-4))
    print('CVC-код: ','#'*len(CVC))
    print('PIN-код: ','&'*(len(PIN)-1)+PIN[-1])
сard(input('Введите 16-ти значный номер карты: '),input('Введите CVC-код: '),input('Введите PIN-код: '))

#2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо
# и справа-налево. Иначе – False. Допишите к функции декоратор, который выведет имя функции, ее аргумент.

print ()
print ("Task №2 :")
def decorator(function):
    def wrapper(arg):
        print('Имя функции: ', str(function.__name__),'\n'
              'Аргумент, отправленный в функцию: ', arg)
        function(arg)
    return wrapper
@decorator
def palindrom(s):
    a=''.join((s.lower().split()))
    a1=a[::-1]
    print(True if a==a1 else False)
palindrom(input('Введите произвольный текст : '))

#3. Дописать в классы Company, Programmer абстрактные методы (хотя бы 1).
# В коде должны быть Private и Protected методы и свойства.

print ()
print ("Task №3 :")
from abc import abstractmethod
class Company:
# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}
# Создайте метод __init__(), внутри которого будут определены два protected свойства:
# 1) _index - передается параметром и 2) _levels - принимает из словаря levels значение с ключом _index
    def __init__(self, index=1):
        self._index = index
        self._levels = Company.levels[self._index]
# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def level_up(self, lev_up):
        self.__is_lead()
        self._index += lev_up
        if self._index <= 4:
            print('Уровень повышен. Новый текуший уровень специалиста в компании :', Company.levels[self._index])
        else:
            print('Повысить уровень невозможно. Текуший уровень специалиста в компании : lead')
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def __is_lead(self):
        if self._index >= 4:
            print('Уровень специалиста в компании : lead. Программист достиг последней квалификации')
        else:
            print('Квалификации данного специалиста в компании может быть повышена')


    @abstractmethod
    def gender(self, g):
        pass
    @abstractmethod
    def zp(self, ok):
        pass
# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):
#Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
#1) name - передается параметром, является публичным, 2)age - возраст
#3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, index, g, ok):
        super().__init__(index)
        self.name = name
        self.age = age
        self.__levels = Company.levels[index]
        self._gender = g
        self._ok = ok
# Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
    def work(self, lev_up=1):
        print('Работа проведена успешно!')
        self.level_up(lev_up)
# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'Имя специалиста: {self.name}')
        print(f'Возраст : {self.age}')
        print(f'Начальный уровень специалиста : {self.__levels}')
        print('Пол сотрудника :',self._gender )
        print(f'Заработная плата сотрудника : {self._zp(self._ok)}')
    def gender(self, g):
        return g
    def _zp(self, ok=1000):
        final_zp = self._index*ok
        return final_zp
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию
# (просто любой текст).
class Spravka:
    @staticmethod
    def knowledge_base():
        text = 'Уметь программировать клёво, жаль, что не просто '
        if True:
            return text

# Тесты
Programmer_1 = Programmer('Коховец Елена', 33, 1, 'Женщина', 2000)
print()
Programmer_1.info()
print()
Programmer_1.work()
print()
Programmer_1.work()
print()
Programmer_1.work()
print()
Programmer_1.work()
print()
print(Spravka.knowledge_base())

#4. Создайте класс на тему животных. Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное. Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию о животных,
# либо о конкретном животном данного класса). Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod, один classmethod, к которым также обратитесь.

print ()
print ("Task №4 :")
class Animals:
    name = 'Слон'
    def __init__(self, name, namber, color, weight):
        self.name = name
        self.namber = namber
        self.__color = color
        self.weight = weight
    def info(self):
        print(f'Текущее название животного: {self.name}')
        print(f'Количество животных: {self.namber}')
        print(f'Цвет животного: {self.__color}')
        print(f'Вес животного : {self.weight}')
    def _walk(self):
        print('Животное ходит')
    @abstractmethod
    def age(self, age):
        pass
    @classmethod
    def name_animal(cls, name, namber, color, weight):
        animal_name = cls(name, namber, color, weight)
        print(f'Название животного: {animal_name.name} / Кол-во животных: {animal_name.namber} / Цвет: {animal_name.__color} / Вес: {animal_name.weight}')
    @staticmethod
    def default_info():
        print(f'Название животного по умолчанию: {Animals.name}')
class Elephant(Animals):
    def __init__(self, name, namber, color, weight, age1, lap ):
        self.age1 = age1
        self.lap = lap
        super().__init__(name, namber, color, weight)
    def __chislo_lap(self, lap):
        return lap
    def info(self):
        print(f'Текущее название животного: {self.name}')
        print(f'Количество животных: {self.namber}')
        print(f'Вес животного : {self.weight}')
        print(f'Возраст животного : {self.age(self.age1)}')
        print(f'Число лап : {self.__chislo_lap(self.lap)}')
    def age(self, age1):
        return age1
class Monkey(Animals):
    def __init__(self, name, namber, color, weight):
        super().__init__(name, namber, color, weight)
    def info(self):
        print(f'Текущее название животного: {self.name}')
        print(f'Количество животных: {self.namber}')
        print(f'Вес животного : {self.weight}')


# Тесты
Animals.name_animal('Белка', 1, 'Белый', 20)
print()
animal1 = Animals('Собака', 1, 'Белый', 20)
animal1.default_info()
animal1.info()
animal1._walk()
animal2 = Elephant('Слон',2, 'Серый', 300, 6, 4)
animal2.default_info()
animal2.info()
animal2._walk()
animal2.age(13)
print()
animal3 = Monkey('Обезьяна',5, 'Коричневый', 5)
animal3.default_info()
animal3.info()
animal3._walk()