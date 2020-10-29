"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""


SRC_FILENAME = "task4.txt"
DST_FILENAME = "task4_dst.txt"
NUMERALS = ('Один', 'Два', 'Три', 'Четыре')


try:
    with open(SRC_FILENAME, 'r') as fhs:
        lines = fhs.readlines()

    numbers = [int(line[-2]) for line in lines if line != '\n']
    content = "\n".join(f'{NUMERALS[n - 1]} - {n}' for n in numbers)

    with open(DST_FILENAME, 'w') as fhd:
        fhd.write(content)
except IOError as e:
    print(e)
except (ValueError, IndexError):
    print("Неконсистентные данные")

