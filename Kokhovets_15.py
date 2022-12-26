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

