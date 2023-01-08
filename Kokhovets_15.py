# Если передаю строку: если произведение количества гласных и согласных
# меньше или равно длине строки, то вывести все гласные. Иначе все согласные
# Если передаю число: вывести произведение суммы четных цифр на длину числа
# Использовать len в 1 методе нельзя, вместо len используйте второй метод.

class Schetchik:
    def method_2(self):
        if type(self)==str:
            return len(self)
        elif type(self)==int:
            return len(str(self))
    def method_1(self):
        if type(self)==str:
            glas = 0
            soglas = 0
            masglas = []
            massoglas = []
            for i in self:
                if i in '''а, у, о, ы, и, э, я, ю, ё, е ,a , e, i, o, u, y''':
                    i = i.lower()
                    glas += 1
                    masglas.append(i)
                elif i in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~: 0123456789''':
                    glas += 0
                    soglas += 0
                else:
                    massoglas.append(i)
                    soglas += 1
            if glas * soglas <=len(self): #glas * soglas <=self.method_2(): #не срабатывает, не понимаю почему
                return masglas
            else:
                return massoglas

        elif type(self)==int:
            s = 0
            self_1=str(self)
            for i in self_1:
                if int(i)%2==0:
                    s+=int(i)
            return s * len(str(self))
            # return s *self.method_2()   #не срабатывает, не понимаю почему
vvod = Schetchik
print('Длина строки :', vvod.method_2('abc'))
print('Длина числа :', vvod.method_2(987))
print('Произведение суммы четных цифр на длину числа :', vvod.method_1(666))
print('Метод 1 от строки :', vvod.method_1('Новый год'))


# Создайте класс Company

class Company:
# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста: 1:junior, 2:middle, 3:senior, 4:lead.
    levels = {1:'junior',2:'middle',3:'senior',4:'lead'}
# Создайте метод __init__(), внутри которого будут определены два protected свойства: 1) _index - передается параметром и 2) _levels - принимает из словаря levels значение с ключом _index
    def __init__(self, index, level1):
        self._index = index
        self._levels = level1     #levels[self._index]
# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def level_up (self, lev_up):
        self._index += lev_up
        print('Уровень повышен. Текуший уровень специалиста в компании :', self._index) #levels[self._index]
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead (self, index):
        if self._index ==0:
            print('Уровень специалиста в компании : lead. Программист достиг последней квалификации')
        else: print('Квалификации данного специалиста в компании может быть повышена')

# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):
# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства: 1) name - передается параметром, является публичным, 2)age - возраст 3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, index, level1):
        super().__init__(index, level1)
        self.name = name
        self.age = age
        self._levels = level1
# Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
    def work(self, lev_up):
        self.level_up (lev_up)
        print('Отличная работа. Уровень специалиста повышен')

# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'Имя : {self.name}')
        print(f'Возраст : {self.age}')
        print(f'Индекс : {self._index}')
        print(f'Уровень специалиста : {self._levels}')
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).

Programmer_1= Programmer('Елена', 33, 1, 'junior')
Programmer_1.info()
Programmer_1.work(2)
Programmer_1.is_lead(0)


