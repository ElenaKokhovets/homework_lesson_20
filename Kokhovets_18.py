# #Task 1
# print('Task 1')
# # Создать в БД таблицу на 10 или более записей.
import sqlite3
conn1 = sqlite3.connect('Kokhovets_18_task1.db')
cursor = conn1.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tb_task1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )'''
)
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Елена')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Анна')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Дима')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Алексей')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Оксана')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Илья')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Иван')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Слава')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Света')''')
cursor.execute('''INSERT INTO tb_task1(name) VALUES('Вася')''')
conn1.commit()
cursor.execute('''SELECT * FROM tb_task1''')
print(*cursor)

# Удалите половину записей.
cursor.execute('''DELETE FROM tb_task1 WHERE id%2 == 0''')
conn1.commit()
cursor.execute('''SELECT * FROM tb_task1''')
print(*cursor)

#Task 2
# Создать две таблицы в одной базе данных.
# Одна таблица будет содержать текстовые данные в единственной колонке
# (не считая id),
# вторая таблица только числовые данные в единственной колонке
# (не считая id).
print()
print('Task 2')
conn2 = sqlite3.connect('Kokhovets_18_task2.db')
cursor_text = conn2.cursor()
cursor_int = conn2.cursor()
cursor_text.execute('''CREATE TABLE IF NOT EXISTS tb_text(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slovo TEXT
    )'''
)
cursor_int.execute('''CREATE TABLE IF NOT EXISTS tb_int(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chislo INT
    )'''
)
# В любом месте кода создайте список
# (например sp = [1,2,3,4,10,100,1000, 'one' , 'potato', 'carrot'],
# в котором будут числа и слова.
sp = [1, 2, 3, 4, 10, 100, 1000, 'one', 'potato', 'carrot']
# Ну а теперь - что с этим делать:
# 1. В текстовую таблицу закинуть все слова, а в числовую все числа.
for i in sp:
    if type(i) == str:
        cursor_text.execute('''INSERT INTO tb_text(slovo) VALUES(?)''', (i,))
    else:
        cursor_int.execute('''INSERT INTO tb_int(chislo) VALUES(?)''', (i,))
conn2.commit()
cursor_text.execute('''SELECT * FROM tb_text''')
print(*cursor_text)
cursor_int.execute('''SELECT * FROM tb_int''')
print(*cursor_int)

# 2. В числовой таблице удалить все строки, где число больше 10.
cursor_int.execute('''SELECT * FROM tb_int''')
chisla = cursor_int.fetchall()
for i in chisla:
    if i[1] > 10:
        cursor_int.execute('''DELETE FROM tb_int WHERE id=?''', (i[0],))
        conn2.commit()
cursor_int.execute('''SELECT * FROM tb_int''')
print(*cursor_int)

# 3. В текстовой таблице все строки со словами длиннее 4 символов обновить на фразу 'Overone‘
cursor_text.execute('''SELECT * FROM tb_text''')
text = cursor_text.fetchall()
for i in text:
    if len(i[1]) > 4:
        cursor_text.execute('''UPDATE tb_text SET slovo='Overone' WHERE id=?''', (i[0],))
        conn2.commit()
cursor_text.execute('''SELECT * FROM tb_text''')
print(*cursor_text)

#Task 3
# Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
print()
print('Task 3')
conn3 = sqlite3.connect('Kokhovets_18_task3.db')
cursor_songs = conn3.cursor()
cursor_songs.execute('''CREATE TABLE IF NOT EXISTS tb_songs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    length INT    
    )'''
)
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Dehumanized — Disturbed',211)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Silence — THEY',213)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Пора возвращаться домой — Би-2, Oxxxymiron', 288)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Страна дождей — Noize MC', 138)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Deadcrush — alt-J',231)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Beggin For Thread — BANKS',250)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('The Way I Am — Staind', 218)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('Fall Again — Kenny G, Robin Thicke',254)''')
cursor_songs.execute('''INSERT INTO tb_songs(name,length) VALUES('По полям, по полям Синий трактор едет к нам', 30)''')
conn3.commit()
cursor_songs.execute('''SELECT * FROM tb_songs''')
print(*cursor_songs)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд
# и записать их в текстовый файл (название и время)
tf = open('songs_task3.txt', 'w+')
cursor_songs.execute('''SELECT * FROM tb_songs''')
songs = cursor_songs.fetchall()
for i in songs:
    if i[2] > 60:
        stroka = i[1]+' - '+str(i[2])
        tf.write(f'{stroka} \n')
    elif i[2] < 60:
        cursor_songs.execute('''DELETE FROM tb_songs WHERE id=?''', (i[0],))
        conn3.commit()
cursor_songs.execute('''SELECT * FROM tb_songs''')
print(*cursor_songs)
