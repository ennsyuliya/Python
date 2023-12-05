# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки 
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и 
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.



class Date:
    __date: str

    def __init__(self, date: str) -> None:
        self.__date = date

    @staticmethod
    def is_valid(date: str):

        day: int
        month: int
        year: int

        try:
            day, month, year = Date.split_to_numb(date)
        except:
            return False

        if not 1 <= month <= 12:
            return False

        if not 0 <= year:
            return False

        if not 1 <= day <= 31:
            return False

        # test over 30
        if month in [4, 6, 9, 11] and day == 31:
            return False

        # test February
        if (
                month == 2 and
                day == 29 and
                year % 4 != 0 and
                year % 100 != 0 and
                year % 400 != 0
        ):
            return False

        return True

    @classmethod
    def split_to_numb(cls, date: str):
        try:
            return(list(map(int, date.split("-"))))
        except:
            raise ValueError("can't split by integer")


#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя 
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("input a: "))
        b = float(input("input b: "))
    except:
        print("incorrect input")
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv("We try div by zero")
        print(f"All is ok {a}/{b} = {a/b}")
    except MyZeroDiv as ex:
        print(ex)


# 3.  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь 
# сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, 
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
# Вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить 
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NoAllNumb(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":

    lst = []
    while True:
        try:
            inp = input()
            if inp == "stop":
                break
            elif not inp.isdigit():
                raise NoAllNumb()
            else:
                lst.append(int(inp))
        except NoAllNumb:
            print("You are input not a number")

    print(*lst)



