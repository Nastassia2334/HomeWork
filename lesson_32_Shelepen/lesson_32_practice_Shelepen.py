# task1
# рекурсивная функция получения факториала числа n

def factorial(n):
    while n != 0:
        return n * (factorial(n - 1))
    else:
        return 1


num = int(input("Введите число: "))
print(factorial(num))

# последовательность фиббоначи
n = int(input("число для фиббоначе: "))
a, b = 0, 1
while b <= n:
    a, b = b, a + b
    print(a)

# создать словарь из двух словарей и отсортировать по длинне ключей
dict_1 = {'верный': [11, 55.2, 'слон'],
          'фиолетовый': 15, 'орда': 'восемь'}
dict_2 = {'ода': {52, 99, 2}, 'сороконожка': {110, 'слово', 15}}
dict_3 = {}
# добавляем в новый словарь
dict_3.update(dict_1)
dict_3.update(dict_2)

new_dict = {}
list_k = list(dict_3.keys())
# сортировка ключей
list_k.sort(key=len)
for i in list_k:
    new_dict[i] = dict_3[i]
print(new_dict)


# task2
# без знаков припинания
def task_1(a):
    new_str = ''
    f = ['.', ',', '?']
    for i in a:
        if i not in f:
            new_str += i
    return new_str


# без букв верхнего регистра
def task_2(a):
    new_str = ''
    for i in a:
        if i.isupper():
            pass
        else:
            new_str += i
    return new_str


# всю строку в верхнем регистре
def task_3(a):
    return a.upper()


# изменить регистр вверхний - нижний и наоборот
def task_4(a):
    new_str = ''
    for i in a:
        if i.isupper():
            new_str += i.lower()
        else:
            new_str += i.upper()
    return new_str


# заменить все знаки препинания на пробелы
def task_5(a):
    new_str = ''
    f = '.,?'
    for i in a:
        if i in f:
            new_str += " "
        else:
            new_str += i
    return new_str


string_ = "Что это было?...Я не ожидал увидеть подобного, но мне придется принять решение"
print(task_1(string_))
print(task_2(string_))
print(task_3(string_))
print(task_4(string_))
print(task_5(string_))
