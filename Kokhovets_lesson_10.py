# ДЗ на понедельник:
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os
os.mkdir('C:/Users/User/Desktop/Lesson_10 ')
with open('C:/Users/User/Desktop/Lesson_10/test_1.txt', 'w'):
    pass
with open('C:/Users/User/Desktop/Lesson_10/test_2.txt', 'w'):
    pass
with open('C:/Users/User/Desktop/Lesson_10/test_3.txt', 'w'):
    pass
os.rename('C:/Users/User/Desktop/Lesson_10/test_1.txt', 'C:/Users/User/Desktop/Lesson_10/rename_1.txt')
os.rename('C:/Users/User/Desktop/Lesson_10/test_2.txt', 'C:/Users/User/Desktop/Lesson_10/rename_2.txt')
os.rename('C:/Users/User/Desktop/Lesson_10/test_3.txt', 'C:/Users/User/Desktop/Lesson_10/rename_3.txt')
os.remove('C:/Users/User/Desktop/Lesson_10/rename_1.txt')
os.remove('C:/Users/User/Desktop/Lesson_10/rename_2.txt')
os.remove('C:/Users/User/Desktop/Lesson_10/rename_3.txt')
os.rmdir('C:/Users/User/Desktop/Lesson_10')
