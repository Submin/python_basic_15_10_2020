"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе.
"""

var_list = []

var_list.extend([True, 0, 1, 2, 'some string', '', 53.1, b'bytes string', {'name': 'Вася'},
                 bytearray(b'bates arra'), (1,), {1,2,1,3}, ValueError, None, {}])

var_list.append(var_list)

for item in var_list:
    item_type = type(item)

    print(f'{item} has {item_type} type',
          '     and is', ('false', 'true')[bool(item)])
