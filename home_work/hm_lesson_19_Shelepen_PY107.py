# Task1
# напишите декоратор, который будет считать
# сколько раз была вызвана декорируемая функция
# вариант 1
def decorator(func):
    def wrapper():
        global result
        func()
        result += 1
        return result

    return wrapper


@decorator
def create_list_gen():
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]
    return list_


result = 0
create_list_gen()
create_list_gen()
print(result)


# вариант 2
def decorator(func):
    result_ = 0

    def wrapper():
        nonlocal result_
        func()
        result_ += 1
        print(result_)

    return wrapper


@decorator
def create_list_gen():
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]
    return list_


create_list_gen()
create_list_gen()


# HomeWork
#написать декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми
#передаваемыми аргументами), а затем — какое значение она возвращает. После этого выводится результат её выполнения
def debug(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(f"Вызвана функция {func.__name__} с аргументами {args}, {kwargs}")
        print(f"возращает значение {a}")
        return a

    return wrapper


@debug
def func_add(num, b, c):
    sum_ = num + b + c
    return sum_


print("результат выполнения функции", func_add(6, b=4, c=5))


