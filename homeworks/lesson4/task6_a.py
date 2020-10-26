"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение
элементов списка будет прекращено.
"""
from typing import Callable
from itertools import count, takewhile

number_types = (int, float, complex)


def my_count(start: number_types = 0, step: number_types = 1):
    """
    Аналог itertools.count создает бесконейчный итератор начиная с start с шагом step
    :param start: число с которого необходимо начать генерацию
    :param step: число на которое различаются сгенерированное и предшествующее числа
    """
    while True:
        yield start
        start += step


def get_count_list1(func: Callable, start: int = 0, stop: int = 10) -> list:
    """
    Возвращает список чисел сгенерированных с помощью кастомной функции my_count в цикле while
    Генерация происходит до stop
    :param func: функция создающая генератор
    :param start: число. с которого начинается генерация
    :param stop: число. до которого происходит генерация
    :return: снкекрированный список
    """
    items = []

    iterable = func(start, 1)

    while True:
        item = next(iterable)
        if item >= stop:
            break

        items.append(item)

    return items


def get_count_list2(func: Callable, start: int = 0, stop: int = 10) -> list:
    """
    Возвращает список чисел сгенерированных с помощью кастомной функции my_count в цикле for/ На 2 строки лаконичней
    Генерация происходит до stop
    :param func: функция создающая генератор
    :param start: число. с которого начинается генерация
    :param stop: число. до которого происходит генерация
    :return: снкекрированный список
    """
    items = []

    for item in func(start, 1):
        if item >= stop:
            break

        items.append(item)

    return items


if __name__ == '__main__':
    start = 3
    stop = 10

    itertools_count_list1 = get_count_list1(count, start, stop)
    print(f"get_count_list1(itertools.count)", itertools_count_list1)

    custom_my_count_list1 = get_count_list1(my_count, start, stop)
    print('get_count_list1(custom my_count)', custom_my_count_list1)

    itertools_count_list2 = get_count_list2(count, start, stop)
    print(f"get_count_list2(itertools.count)", itertools_count_list2)

    custom_my_count_list2 = get_count_list2(my_count, start, stop)
    print('get_count_list2(custom my_count)', custom_my_count_list2)

    exotic_count_list = list(takewhile(int(stop).__gt__, count(start, 1)))
    print('exotic_count_list', exotic_count_list)
