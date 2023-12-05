# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_sum(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')


print(my_sum(int(input('Первое число: ')), int(input('Второе число: '))))


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

firstname = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int (input('Введите год рождения '))
city = input('Введите ваш город: ')
email = input('Введите ваш e-mail: ')
phone = input('Введите ваш телофон: ')

print('Имя ', firstname, 'фамилия ', surname, ', год рождения  ', age, ', город ', city,', e-mail', email,', телефон ', phone)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c
try:
    num_1 = int(input('Введите число а '))
    num_2 = int(input('Введите число b '))
    num_3 = int(input('Введите число с '))
    print(f'Сумма двух максимальных чисел равна:  {my_func(num_1, num_2, num_3)}')
except ValueError as e:
    print(f'{e}')


# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y. 
# Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
#  Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func():
    try:
        x = float(input("Укажите действительное положительное число x: "))
        y = float(input("Укажите целое отрицательное число y: "))
    except ValueError:
        return
    result = x ** y
    return result

print( my_func())


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
#  Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
#  Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и 
# после этого завершить программу.

def my_sum(my_list):
    items_sum = 0
    for item in my_list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_my_string(s):
    s = s.replace('#', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return my_sum(numbers)


numbers_sum = 0

while True:
    numbers_sting = input("Введите строку чисел, разделенных пробелом. Для завершения введите символ '#'\n")
    numbers_sum += sum_my_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Сумма значений элементов {numbers_sum}")
    if numbers_sting.count('#') > 0:
        break


#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text.

def int_func(word: str):
    first_char = word[:1]
    big_first_char = first_char.upper()
    tail = word[1:]
    return big_first_char + tail


def int_func_ext(row: str):
    result = []
    words = row.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Введите строку для преобразования:\n")
print(f"{int_func_ext(s)}")





