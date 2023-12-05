# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

with open('test1.txt', 'w') as file:
    input_line= input('text: \n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line=input('text: \n')


#2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

lines = 0
letters = 0
out_f = open("out_file.txt", "w")
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
out_f.writelines(str_list)
out_f.close()
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
for line in open('out_file.txt', 'r'):
    lines += 1
    letters += len(line)
print("Lines:", lines)
print("Letters:", letters)


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников. Пример файла:
# Иванов 23543.12
# Петров 13749.32
poor = []
sal = []
new3_f = open('hw5-3.txt', 'w', encoding='utf-8')
str_list = ['Иванов 23543\n', 'Петров 36452\n', 'Сидоров 36452\n', 'Зуев 3526\n', 'Глазунов 28511\n', 'Карнаухов 13524\n','Попов 47521\n', 'Зайцев 11235\n', 'Пойлов 13495\n', 'Смирнов 13548\n']
new3_f.writelines(str_list)
new3_f.close()
for i in str_list:
    i = i.split()
    if int(i[1]) < 20000:
        poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}

text_en = ''
with open('task4.txt') as file, open('new_file.txt','w', encoding='UTF-8') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data= line.split()
        rus_num = nums.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_num)}')


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()


# 6. Сформировать (не программно) текстовый файл.
#В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических
#и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result = {}

with open('task6.txt',  encoding='UTF-8') as file:
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    hours = 0
    for elem in data[1:]:
        if elem != '-':
            num = 0
            for i in elem:
                if i.isdigit():
                    num += 1
                else:
                    break
            hours += int(num)
    result.update({data[0].strip(':'):hours})
print(result)


#7. #Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
companies = {}
pos_count, pos_sum = 0, 0
with open('task7.txt') as file:
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    profit = float (data [2]) - float (data [3])
    companies.update({data[0]:profit})
    if profit > 0:
        pos_count += 1
        pos_sum += pos_count

averge_profit = pos_sum / pos_count
result = [companies, {'averge_profit':averge_profit}]

with open('result.json','w',  encoding='utf-8') as file:
    json.dump(result, file)

with open('result.json', encoding='utf-8') as file:
    result = json.load(file)
    print(result)





