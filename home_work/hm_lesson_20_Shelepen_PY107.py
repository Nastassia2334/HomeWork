# Home work
# Реализуйте итератор колоды карт (52 штуки) CardDeck.
# Каждая карта представлена в виде строки типа «2 пик».
# при вызове функции next() будет представлена
# следующая карта. По окончании перебора всех
# элементов возникнет ошибка StopIteration

def CardDeck(card_value, card_suit):
    x = 1
    list_card = []
    if x > len(list_card):
        raise StopIteration
    else:
        for i in card_suit:
            for u in card_value:
                list_card.append(u + " " + i)
                x += 1
        return list_card


value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suit = ['пик', 'треф', 'червей', 'бубен']

next_card = CardDeck(value, suit)
h = iter(next_card)


# Home Work 2
# Создайте функцию infinite(lst, tries),
# которая будет проходиться по элементам списка lst (целые числа) заданное количество раз (tries) циклически.
# Один раз - один элемент списка.
# После вывода последнего значения последовательности процедура начнется с самого начала.
# Результат работы функции представьте в виде строки, состоящей из tries количества символов.


def infinite(lst, tries):
    t = 1
    k = iter(lst)
    while t <= tries:
        try:
            iter_lst = next(k)
            print(iter_lst)
            t += 1
        except StopIteration:
            k = iter(lst)
    else:
        print('цикл закончен')
        pass


list_list = [1, 2, 3, 4, 5, 6, 7, 8]
num = int(input("Введите количество альтераций: "))
infinite(list_list, num)
