"""
Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""


FILENAME = "myfile.txt"

while True:
    user_input = input('Введите произвольную строку: ')
    if not user_input:
        break

    try:
        with open(FILENAME, 'w') as fh:
            fh.write(f'{user_input}\n')
    except IOError as e:
        print(e)
        break
