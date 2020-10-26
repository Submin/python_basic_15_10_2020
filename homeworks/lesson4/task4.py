"""
Представлен список чисел. Определить элементы списка, не имеющие
повторений. Сформировать итоговый массив чисел, соответствующих
требованию. Элементы вывести в порядке их следования в исходном
списке. Для выполнения задания обязательно использовать генератор.
"""
from typing import Iterable, Callable
from itertools import filterfalse


def my_filterfalse(func: Callable, iterable: Iterable) -> None:
    """
    Создает итератор элементы которого отсортированы в соответствии с отрицанием func
    :param func: функция в соответствии с отрицанием которой происходит фильтрация исходного объекта iterable
    :param iterable: исходный итерируемы объект
    """

    def default_func(x):
        """
        если func = None используется эта функция
        :param x: объект приводимый к True или False
        :return: тот же объект в контексте будева значения
        """

        return x

    func = default_func if func is None else func

    for i in iterable:
        if not func(i):
            yield i


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа разделяя их пробелами: ')

    try:
        source_list = tuple(map(int, input_data.split()))
    except ValueError:
        print('Неверно введенные данные')
        exit(1)

    # source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    print('itertools drophile', list(filterfalse(lambda x: source_list.count(x) > 1, source_list)))
    print('custom drophile', list(my_filterfalse(lambda x: source_list.count(x) > 1, source_list)))
