"""
Представлен список чисел. Необходимо вывести элементы исходного
списка, значения которых больше предыдущего элемента.
"""


def find_big(iterable: list):
    """ Ищет большие числа в списке
    :param iterable: списой целых чисел
    """
    tmp = iterable[0]

    for i in iterable:
        if not isinstance(i, int):
            raise TypeError(f"Function not support type '{i.__class__.__name__}'")

        if i > tmp:
            yield i

        tmp = i


if __name__ == '__main__':
    source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

    generator = find_big(source_list)
    print(list(generator))
