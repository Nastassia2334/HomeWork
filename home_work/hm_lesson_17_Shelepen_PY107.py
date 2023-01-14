# Calculator
class Calculator:
    def __init__(self):
        self.num_input()

    def num_input(self):
        try:
            self.num_1 = int(input("введите число: "))
            self.num_2 = int(input("введите число: "))
        except ValueError:
            print("введите правильные значения")
            self.num_1 = int(input("введите число: "))
            self.num_2 = int(input("введите число: "))

    def func_addition(self):
        add = self.num_1 + self.num_2
        return add

    def func_subtraction(self):
        sub = self.num_1 - self.num_2
        return sub

    def func_multiplication(self):
        mul = self.num_1 * self.num_2
        return mul

    def func_division(self):
        try:
            div = self.num_1 / self.num_2
        except ZeroDivisionError:
            return "невозможность деления на 0"
        else:
            return div


while True:
    result = Calculator()
    symb_ = input("введите символ вычисления (+-*/) для выхода(end): ")
    if symb_ == '+':
        print(result.func_addition())
    elif symb_ == '-':
        print(result.func_subtraction())
    elif symb_ == '*':
        print(result.func_multiplication())
    elif symb_ == '/':
        print(result.func_division())
    elif symb_ == 'end':
        print("вычисления завершены")
        break
    else:
        print("проверьте верность введенных символов")


# Homework
class Exercise:
    def __init__(self, attr):
        self.string_ = attr

    def type_(self):
        if self.string_.isalpha():
            counter_vowels = []
            counter_consonants = []
            for attr in self.string_:
                if attr in "ауоиэыяюеё":
                    counter_vowels.append(attr)
                else:
                    counter_consonants.append(attr)
            if len(counter_vowels) * len(counter_consonants) <= result.length():
                return counter_vowels
            else:
                return counter_consonants

        if self.string_.isdigit():
            num_ = int(self.string_)
            counter_even = 0
            while num_ > 0:
                if num_ % 2 == 0:
                    counter_even += num_ % 10
                num_ = num_ // 10

            return counter_even * result.length()

    def length(self):
        return len(self.string_)


string_ = input("введите слово или число: ")
result = Exercise(string_)
result.length()
print(result.type_())
