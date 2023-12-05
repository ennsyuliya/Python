# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    color=['Красный', 'Желтый', 'Зеленый']


    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

t = TrafficLight()
t.running()

#2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    length = []
    width = []

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')

r = Road(5000, 20)
r.asphalt_mass()


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name (self):
        return self.name + ' ' + self.surname

    def get_total_income (self):
        return self._income['wage'] + self._income['bonus']

p = Position('Maxim', 'Ivanov', 'MO', int('75000'), int ('15000'))
print(p.get_full_name(), p.get_total_income())


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop (self, speed):
        print('Stop')

    def turn(self, direction):
        print(f'Car turned to {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')

class PoliceCar (Car):
    def __init__(self,speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar (70, 'red', 'Sport')
sport = SportCar (100, 'yellow', 'Sport')
work = WorkCar (35, 'green', 'Work')
police = PoliceCar (90, 'black', 'Police')

town.show_speed()
work.show_speed()

town.show_speed = 30
work.show_speed()

police.turn('left')


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw (self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw (self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw (self):
        print(f'Запуск отрисовки карандашем {self.title}')


class Handle(Stationery):
    def draw (self):
        print(f'Запуск отрисовки маркером {self.title}')

pen = Pen ('A')
pensil = Pencil ('B')
handle = Handle ('C')
for s in (pen, pensil, handle):
    s.draw()

