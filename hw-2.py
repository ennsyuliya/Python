# Создать список и заполнить его элементами различных типов данных.Реализовать cкрипт
# проверки типа данных каждого элемента.Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_l = [3, 8, 97.2, "text", "word", True, None]

for item in my_l:
    print(type(item))


#Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

print('Первый вариант')
string = input('Введите элемент ')
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
symbols[el] = symbols[len(string) - el - 1]
symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)

print('второй вариант')

list = input("Введите элементы списка ")
my_list = list[::-1]
print(my_list)
# если ввести буквы как-то затрудняюсь

print('Третий вариант')
var_1, var_2, var_3, var_4 = input('Введите элемент (4 знака)  ')
print(var_1, var_2, var_3, var_4)
var_1, var_2, var_3, var_4 = var_2, var_1, var_4,var_3
print(var_1, var_2, var_3, var_4)


# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('Решение через list')


def season(m):
    if m == 12 or m == 1 or m == 2:
        return 'Это зима'
    elif m == 3 or m == 4 or m == 5:
        return 'Это весна'
    elif m == 6 or m == 7 or m == 8:
        return 'Это лето'
    elif m == 9 or m == 10 or m == 11:
        return 'Это осень'
    else:
        return 'Нет такого месяца'
result = season(int(input('Введите номер месяца: ')))
print(result)

print('Решение через dict')
seasons_list = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month_dict = int(input('Введите месяц: '))
for key in seasons_list.keys():
    if month_dict in seasons_list[key]:
        print(key)


#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_string = input('Введите строку: ')
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1


# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
digit = int(input('Введите число:  '))
while digit != 0:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f'текущий список - {my_list}')
    digit = int(input('Введите число: '))





    




