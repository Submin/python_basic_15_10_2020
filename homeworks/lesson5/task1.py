"""
Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""

filename = "myfile.txt"

try:
    with open(filename, 'w', encoding='utf-8') as file:
        while True:
            user_input = input('Введите произвольную строку: ')
            if not user_input:
                break

            file.write(f'{user_input}\n')
except (IsADirectoryError, PermissionError) as e:
    print(e)
