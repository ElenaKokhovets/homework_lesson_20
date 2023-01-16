import sys

# from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

from PyQt5.Qt import *

from PyQt5 import QtGui

#QApplication-виджет для вызова окна приложения
#QLabel виджет для создания окна с текстов
#QPushButton виджет для создания и работы кнопок
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() #метод для делегирования создания GUI
        self.my_input = '0' #результат вычисления
        self.operand_1 = 0 #первое число в вычислении
        self.operand_2 = 0 #второе число в вычислении
        self.operation = '0'  # операция

    def initUI(self): #внешний вид калькулятора
        self.setGeometry(0, 0, 225, 430)    #координаты верхнего левого угла, ширина окна,высота окна
        self.setWindowTitle('Калькулятор')    #задаём имя окна
        self.label = QLabel(self) #задаём первое поле для ввода /вывода результата
        self.label.setText('Введите число') #установили начальное значение в окне   (то что отображается в окошке)
        self.label.resize(225,95) #ширина и высота лейбла, размер окна
        self.label.move(5, 0)  # ширина и высота лейбла, размер окна
        self.label.setFont(QtGui.QFont('Isocpeur',14,italic=True))



        #ишем название кнопок всегда через селф
        self.num_1 = QPushButton('1', self)  #создали кнопку и подписали её как 1
        self.num_1.resize(50, 50) #меняем размер кнопки
        self.num_1.move(5, 100)  # меняем размер кнопки
        self.num_1.setFont(QtGui.QFont('Isocpeur', 14, italic=True))


        self.num_2 = QPushButton('2', self)  # создали кнопку и подписали её как 1
        self.num_2.resize(50, 50)  # меняем размер кнопки
        self.num_2.move(60, 100)  # меняем размер кнопки
        self.num_2.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_3 = QPushButton('3', self)  # создали кнопку и подписали её как 1
        self.num_3.resize(50, 50)  # меняем размер кнопки
        self.num_3.move(115, 100)  # меняем размер кнопки
        self.num_3.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_4 = QPushButton('4', self)  # создали кнопку и подписали её как 1
        self.num_4.resize(50, 50)  # меняем размер кнопки
        self.num_4.move(5, 155)  # меняем размер кнопки
        self.num_4.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_5 = QPushButton('5', self)  # создали кнопку и подписали её как 1
        self.num_5.resize(50, 50)  # меняем размер кнопки
        self.num_5.move(60, 155)  # меняем размер кнопки
        self.num_5.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_6 = QPushButton('6', self)  # создали кнопку и подписали её как 1
        self.num_6.resize(50, 50)  # меняем размер кнопки
        self.num_6.move(115, 155)  # меняем размер кнопки
        self.num_6.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_7 = QPushButton('7', self)  # создали кнопку и подписали её как 1
        self.num_7.resize(50, 50)  # меняем размер кнопки
        self.num_7.move(5, 210)  # меняем размер кнопки
        self.num_7.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_8 = QPushButton('8', self)  # создали кнопку и подписали её как 1
        self.num_8.resize(50, 50)  # меняем размер кнопки
        self.num_8.move(60, 210)  # меняем размер кнопки
        self.num_8.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_9 = QPushButton('9', self)  # создали кнопку и подписали её как 1
        self.num_9.resize(50, 50)  # меняем размер кнопки
        self.num_9.move(115, 210)  # меняем размер кнопки
        self.num_9.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.num_0 = QPushButton('0', self)  # создали кнопку и подписали её как 1
        self.num_0.resize(50, 50)  # меняем размер кнопки
        self.num_0.move(60, 265)  # меняем размер кнопки
        self.num_0.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.plus = QPushButton('+', self)  # создали кнопку и подписали её как 1
        self.plus.resize(50, 50)  # меняем размер кнопки
        self.plus.move(170, 210)  # меняем размер кнопки
        self.plus.setStyleSheet('background-color: lightgreen')
        self.plus.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.minus = QPushButton('-', self)  # создали кнопку и подписали её как 1
        self.minus.resize(50, 50)  # меняем размер кнопки
        self.minus.move(170, 265)  # меняем размер кнопки
        self.minus.setStyleSheet('background-color: lightgreen')
        self.minus.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.mul = QPushButton('*', self)  # создали кнопку и подписали её как 1
        self.mul.resize(50, 50)  # меняем размер кнопки
        self.mul.move(170, 155)  # меняем размер кнопки
        self.mul.setStyleSheet('background-color: lightgreen')
        self.mul.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.div = QPushButton('/', self)  # создали кнопку и подписали её как 1
        self.div.resize(50, 50)  # меняем размер кнопки
        self.div.move(170, 100)  # меняем размер кнопки
        self.div.setStyleSheet('background-color: lightgreen')
        self.div.setFont(QtGui.QFont('Isocpeur', 14, italic=True))

        self.ravn = QPushButton('=', self)  # создали кнопку и подписали её как 1
        self.ravn.resize(160, 50)  # меняем размер кнопки
        self.ravn.move(5, 375)  # меняем размер кнопки
        self.ravn.setStyleSheet('background-color: lightblue')
        self.ravn.setFont(QtGui.QFont('Isocpeur', 14, italic=True))


        self.clear = QPushButton('C', self)  # создали кнопку и подписали её как 1
        self.clear.resize(50, 50)  # меняем размер кнопки
        self.clear.move(170, 375)  # меняем размер кнопки
        self.clear.setFont(QtGui.QFont('Isocpeur', 14, italic=True))
        self.clear.setStyleSheet('background-color: blue')

        self.deg_y = QPushButton('x^y', self)  # создали кнопку и подписали её как 1
        self.deg_y.resize(50, 50)  # меняем размер кнопки
        self.deg_y.move(115, 320)  # меняем размер кнопки
        self.deg_y.setFont(QtGui.QFont('Isocpeur', 14, italic=True))
        self.deg_y.setStyleSheet('background-color: lightgreen')

        self.sqr_y = QPushButton('y√x', self)  # создали кнопку и подписали её как 1
        self.sqr_y.resize(50, 50)  # меняем размер кнопки
        self.sqr_y.move(170, 320)  # меняем размер кнопки
        self.sqr_y.setFont(QtGui.QFont('Isocpeur', 14, italic=True))
        self.sqr_y.setStyleSheet('background-color: lightgreen')

        self.deg_y2 = QPushButton('x^2', self)  # создали кнопку и подписали её как 1
        self.deg_y2.resize(50, 50)  # меняем размер кнопки
        self.deg_y2.move(5, 320)  # меняем размер кнопки
        self.deg_y2.setFont(QtGui.QFont('Isocpeur', 14, italic=True))
        self.deg_y2.setStyleSheet('background-color: lightgreen')

        self.sqr_y2 = QPushButton('2√x', self)  # создали кнопку и подписали её как 1
        self.sqr_y2.resize(50, 50)  # меняем размер кнопки
        self.sqr_y2.move(60, 320)  # меняем размер кнопки
        self.sqr_y2.setFont(QtGui.QFont('Isocpeur', 16, italic=True))
        self.sqr_y2.setStyleSheet('background-color: lightgreen')

        self.num_1.clicked.connect(self.one) # привязка у кнопке
        self.num_2.clicked.connect(self.two)  # привязка у кнопке
        self.num_3.clicked.connect(self.tree)  # привязка у кнопке
        self.num_4.clicked.connect(self.four)  # привязка у кнопке
        self.num_5.clicked.connect(self.five)  # привязка у кнопке
        self.num_6.clicked.connect(self.six)  # привязка у кнопке
        self.num_7.clicked.connect(self.seven)  # привязка у кнопке
        self.num_8.clicked.connect(self.eight) # привязка у кнопке
        self.num_9.clicked.connect(self.nine)  # привязка у кнопке
        self.num_0.clicked.connect(self.zero)  # привязка у кнопке
        self.plus.clicked.connect(self.plus_1)  # привязка у кнопке
        self.minus.clicked.connect(self.minus_1)  # привязка у кнопке
        self.mul.clicked.connect(self.mul_1)  # привязка у кнопке
        self.div.clicked.connect(self.div_1)  # привязка у кнопке
        self.ravn.clicked.connect(self.ravno)  # привязка у кнопке
        self.clear.clicked.connect(self.clean)  # привязка у кнопке
        self.deg_y.clicked.connect(self.deg_1)  # привязка у кнопке
        self.sqr_y.clicked.connect(self.sqr_1)  # привязка у кнопке
        self.deg_y2.clicked.connect(self.deg_2)  # привязка у кнопке
        self.sqr_y2.clicked.connect(self.sqr_2)  # привязка у кнопке

    def enter_value(self):
        if self.label.text() == 'Введите число':
            self.label.setText('') # при запуске калькулятора в label нужно убрать 0 перед вводом
        self.label.setText(str(self.label.text())+str(self.my_input))

    def one (self):
        self.my_input = 1
        self.enter_value()


    def two (self):
        self.my_input = 2
        self.enter_value()

    def tree(self):
        self.my_input = 3
        self.enter_value()

    def four(self):
        self.my_input = 4
        self.enter_value()

    def five(self):
        self.my_input = 5
        self.enter_value()

    def six(self):
        self.my_input = 6
        self.enter_value()

    def seven(self):
        self.my_input = 7
        self.enter_value()

    def eight(self):
        self.my_input = 8
        self.enter_value()

    def nine(self):
        self.my_input = 9
        self.enter_value()

    def zero(self):
        self.my_input = 0
        self.enter_value()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def deg_1(self):
        self.operation = 'x^y'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def sqr_1(self):
        self.operation = 'y√x'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText('Введите число')

    def deg_2(self):
        self.operation = 'x^2'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText(str(self.operand_1 ** 2))

    def sqr_2(self):
        self.operation = '2√x'
        self.operand_1 = float(self.label.text())#запомнили число с которым проводим операцию
        self.label.setText(str(self.operand_1 ** (1 / 2)))

    def clean(self):
        self.label.setText('Введите число')

    def ravno(self):
        self.operand_2 = float(self.label.text())  # запомнили число с которым проводим операцию
        if self.operation == '+':
            self.label.setText(str(self.operand_1+self.operand_2))
        elif self.operation == '-':
            self.label.setText(str(self.operand_1-self.operand_2))
        elif self.operation == '*':
            self.label.setText(str(self.operand_1*self.operand_2))
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.label.setText('На ноль делить нельзя')
            else:
                self.label.setText(str(self.operand_1/self.operand_2))
        elif self.operation == 'x^y':
            self.label.setText(str(self.operand_1 ** self.operand_2))
        elif self.operation == 'y√x':
            self.label.setText(str(self.operand_1 ** (1/self.operand_2)))


app = QApplication(sys.argv)  #создали объект класса QApplication,таким образом создали наше окно
# виджет QApplication вызывает данное окно.В него передаём sys.argv-аргументы командной строки( передали данные виндоуз)
my_calculator = Calculator()  #создали объект класса калькулятор
my_calculator.show()  #показали наш объект
sys.exit(app.exec()) #завершаем работу калькулятора. Если будут ошибки, то придёт уведомление

