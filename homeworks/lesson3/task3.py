"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""
from my_functions import my_sum, my_sorted


def my_func(a, b, c):
    """ Функция вызова расчета суммы двух наибольших чисел
    :param a: порвый позиционный аргумент
    :param b: второй позиционный аргумент
    :param c: третий позиционный аргумент
    :return: результат вычислений
    """
    try:
        sorted_list: list = my_sorted((a, b, c), reverse=True)
        return my_sum(sorted_list[:2])
    except TypeError as e:
        print(f'Вай!!! как не хорошо: {e}')


if __name__ == '__main__':
    unsorted_list = [20, 167, 67.3];
    print(my_func(*unsorted_list))
