# ДЗ на вторник:
# 1. Создать базу данных под своим именем Ivanov.db
import sqlite3
bd = sqlite3.connect('Kokhovets.db')
cursor_bd = bd.cursor()
cursor_Animals = bd.cursor()
# 2. Создать в ней таблицу FIO с тремя полями: имя (текст), фамилия (текст), возраст (число)
cursor_bd.execute(
    '''CREATE TABLE IF NOT EXISTS FIO(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    surname TEXT,
    age INT)'''
)
# 3. Создать вторую таблицу Animals с двумя полями: название животного и возраст животного
cursor_Animals.execute(
    '''CREATE TABLE IF NOT EXISTS Animals(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    animal_name TEXT, 
    animal_age INT)'''
)
# 4. Заполнить каждую таблицу минимум тремя записями
cursor_bd.execute('''INSERT INTO FIO(name, surname, age) VALUES('Elena', 'Kokhovets', 33)''')
cursor_bd.execute('''INSERT INTO FIO(name, surname, age) VALUES('Nina', 'Sinitsyna', 25)''')
cursor_bd.execute('''INSERT INTO FIO(name, surname, age) VALUES('Ivan', 'Ivanov', 19)''')
cursor_Animals.execute('''INSERT INTO Animals(animal_name, animal_age) VALUES('Dog', 5)''')
cursor_Animals.execute('''INSERT INTO Animals(animal_name, animal_age) VALUES('Cat', 4)''')
cursor_Animals.execute('''INSERT INTO Animals(animal_name, animal_age) VALUES('Elephant', 2)''')

bd.commit()
