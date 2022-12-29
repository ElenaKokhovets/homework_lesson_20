# ДЗ на четверг:
# Класс Company:

# Создайте класс Company

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
        self.is_lead()
        self._index += lev_up
        if self._index <= 4:
            print('Уровень повышен. Новый текуший уровень специалиста в компании :', Company.levels[self._index])
        else:
            print('Повысить уровень невозможно. Текуший уровень специалиста в компании : lead')
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index >= 4:
            print('Уровень специалиста в компании : lead. Программист достиг последней квалификации')
        else:
            print('Квалификации данного специалиста в компании может быть повышена')
# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):
#Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
#1) name - передается параметром, является публичным, 2)age - возраст
#3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, index):
        super().__init__(index)
        self.name = name
        self.age = age
        self._levels = Company.levels[index]
# Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
    def work(self, lev_up=1):
        print('Работа проведена успешно!')
        self.level_up(lev_up)
# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'Имя специалиста: {self.name}')
        print(f'Возраст : {self.age}')
        print(f'Начальный уровень специалиста : {self._levels}')
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию
# (просто любой текст).
class Spravka:
    @staticmethod
    def knowledge_base():
        text = 'Уметь программировать клёво, жаль, что не просто '
        if True:
            return text
# Тесты
Programmer_1 = Programmer('Коховец Елена', 33, 1)
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
