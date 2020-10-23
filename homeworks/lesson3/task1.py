"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

from my_functions import my_div

input_patterns = (
    ('Пожалуйста введите делимое: ', float,),
    ('Пожалуйста введите делитель: ', float,),
)


if __name__ == '__main__':
    div_data = []

    while not div_data:
        for item_title, item_type in input_patterns:
            try:
                div_data.append(item_type(input(item_title)))
            except ValueError:
                print("Вводимые данные должны быть числом")
                div_data.clear()

    try:
        quotient = my_div(*div_data)
        print(f'Результа: {quotient}')
    except ZeroDivisionError:
        print('Попытка деления на ноль')
