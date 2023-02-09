import sqlite3
import random

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 TEXT, col_3 TEXT)''')


num_col = int(input("Число: "))

d = "red"
f = "black"
cursor.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES (?,?,?)''', (num_col, d, f))
# сохраняем изменения
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
#выводим каждую запись в отдельной строке
for _ in k:
    print(_)


#Task 2

a = str(random.randint(1, 10))
b = str(random.randint(1, 10))
conn = sqlite3.connect('baza2.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
#заполняем поля рандомно числами
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (a, b))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')

k = cursor.fetchall()
#счетсик количества чисел
count = 0
#сумма чисел
sum_elem = 0
for elem in k:
    print(elem)
    count += len(elem) - 1
    sum_elem += sum(elem[1:])
print(f'сумма {sum_elem},количество {count}')
#вычисляем средне арифметическое
average = sum_elem / count
print(f'среднее арифметическое {average}, количество записей {len(k)}')
#если больше удаляем 4ю запись БД
if average > len(k):
    cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
    conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
print(cursor.fetchall())



#Task 3
a = str(random.randint(1, 10))
b = str(random.randint(1, 10))
conn = sqlite3.connect('baza3.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
#рандомно заполняем поля
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (a, b))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')

k = cursor.fetchall()
for o in k:
    print(o)
h = random.choice(k)
print(h)
h1 = h[0]

#если числа в полях четные то удаляем
if h[1] % 2 == 0 and h[2] % 2 == 0:
    cursor.execute('''DELETE FROM tab_1 WHERE id=?''', (h1,))
    conn.commit()
#если нечетные обновляем данные на 2,2 в полях
if h[1] % 2 == 1 and h[2] % 2 == 1:
    cursor.execute('''UPDATE tab_1 SET col_1 =2, col_2 = 2 WHERE id=?''', (h1,))
    conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
print(cursor.fetchall())

#Task 4
conn = sqlite3.connect('baza4.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()


# создаем класс
class BD:
    # указываем 3 ключевых параметра со значением None
    def bd_tab(self, a=None, b=None, c=None):
        # проверяем на сколько и какие аргументы были переданы в функцию
        # если 1 аргумент
        if a is not None and b is None and c is None:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
            conn.commit()
        # если 2 аргумента и второе число
        if a is not None and b is not None and c is None:
            if type(b) == int:
                cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
                conn.commit()
        # если 3 аргумента и 3й является числом
        if a is not None and b is not None and c is not None:
            if type(c) == int:
                cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3 ''')
                conn.commit()


result = BD()
# result.bd_tab(3)
# result.bd_tab(6, 7)
result.bd_tab(4, 6, 9)

cursor.execute('''SELECT*FROM tab_1''')
new_k = cursor.fetchall()
print(new_k)

#Task 5


conn = sqlite3.connect('baza5.db')
cursor = conn.cursor()
# создаем базу данных с 3 записями
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('day', 'night')''')
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('big', 'small')''')
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('high', 'short')''')
conn.commit()
# удаляем запись 2
cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
# обновляем значения записи 3
cursor.execute('''UPDATE tab_1 SET col_1='hello', col_2='world' WHERE id=3''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
t = cursor.fetchall()
print(k)
# записываем в файл в столбик
with open('baza5.txt', 'w') as file:
    for _ in t:
        for i in _:
            # записываем каждый элемент
            file.write(str(i) + ' ')
        # перенос на новую строку
        file.write('\n')
