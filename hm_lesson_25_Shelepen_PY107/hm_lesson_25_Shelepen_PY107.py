import sqlite3

conn = sqlite3.connect('baza_home.db')
cursor = conn.cursor()
# текстовые данные
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
# числовые данные
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()
# список из чисел и слов
list_num_letter = [1, 8, 'red', 'black', 5, 'yellow', 7, 'white', 4]
for i in list_num_letter:
    # если элемент списка слово
    if type(i) is str:
        len_str = len(i)
        # записываем в таблицу с текстовыми данными
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES(?)''', (i,))
        conn.commit()
        # считакм длинну слова и записываем в таблицу с числовыми данными
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES(?)''', (len_str,))
        conn.commit()
    # если элемент списка число
    elif type(i) is int:
        # проверем четное ли оно
        if i % 2 == 0:
            # четное записываем в таблицу с числами
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (i,))
            conn.commit()
        else:
            # если нечетное то в таблицу с текстовыми данными записываем слово "нечетное"
            num = 'нечетное'
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (num,))
            conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
letters = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_2''')
number = cursor.fetchall()

print(letters)
print(number)
# если во второй таблице больше 5 записей
# удаляем из первой таблицы запись 1
# если меньше меняем в первой таблице первую запись на 'hello'
if len(number) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1='hello' FROM id=1''')
cursor.execute('''SELECT*FROM tab_2''')
number = cursor.fetchall()

print(letters)
print(number)
