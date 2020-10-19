"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

var_list = []

while True:
    item = input('Пожалуйста введите элемент списка: ')
    var_list.append(item)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break

last_idx = len(var_list) - 1

for idx, _ in enumerate(var_list):
    if idx % 2 == 0 and idx < last_idx:
        var_list[idx + 1], var_list[idx] = var_list[idx:idx + 2]

print(var_list)