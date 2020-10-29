"""
Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
"""

FILENAME = "task5.txt"

DIGITS_STR = "12 7.2 87 93.5 0 32 7.1"

summ = 0

try:
    with open(FILENAME, 'w') as fhs:
        fhs.write(DIGITS_STR)

    with open(FILENAME, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        summ += float(item)
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(summ)