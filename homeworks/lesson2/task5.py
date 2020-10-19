"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться
после них.
"""

raiting = []

while True:
    item = input('Пожалуйста введите число: ')
    if not item.isdigit():
        print("Введены некорректные данные. Попробуйте снова")
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(raiting):
        if item > num:
            idx = i
            break

    if idx is None:
        raiting.append(item)
    else:
        raiting.insert(idx, item)

    print(raiting)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break
