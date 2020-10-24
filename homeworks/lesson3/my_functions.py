from typing import Iterable, Callable
from math import sqrt

number_types = (int, float, complex)


def my_div(x: number_types, y: number_types) -> number_types:
    """ Делит число на число
    :param x: Делимое
    :param y: Делитель
    :return: Частное
    """
    if not (isinstance(x, number_types) and isinstance(y, number_types)):
        raise TypeError(f"unsupported operand type(s) for my_div: "
                        f"'{x.__class__.__name__}' and '{y.__class__.__name__}'")

    return x / y


def my_sum(iterable: Iterable, start: number_types = 0) -> [int, float]:
    """ Возвращает сумму элементов iterable и statrt.
    По умолчанию start равен 0. Если iterable пуст, возвращает 0
    Функция работает только с целыми и|или вещественными числами
    иначе выбрасывает исключение
    :param iterable: итерируемый объект с элементами для суммирования
    :param start: значение к которому начинаестся складывание
    :return: сумму start и всех элементов iterable
    """
    # базовые проверки
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{iterable.__class__.__name__}' object is not iterable")

    if not isinstance(start, number_types):
        raise TypeError(f"my_sum() can't sum strings [use ''.join(seq) instead]")

    result = start

    for item in iterable:
        # падаем, если типы не совместимы
        if not isinstance(item, number_types):
            raise TypeError(f"unsupported operand type(s) for +:"
                            f" 'int' and '{item.__class__.__name__}'")

        result += item

    return result


def my_sorted(iterable: Iterable, key: Callable = None, reverse: bool = False, ) -> list:
    """ Функция сортировки реализованная на алгоритме вставки а
    :param iterable:  итерируемый объект для сортировки
    :param key: функция извлечения объекта, по которому будет производиться сортировка
    :param reverse: направление сортировки: False - в порядке возрастания (по умолчанию)
    :return: отсортированный список
    """
    # выбор направления сортировки
    cmp: Callable = (
        lambda x, y: x > y,  # по возрастанию
        lambda x, y: x < y,  # по убыванию
    )[reverse]

    # функция извлечения - если отсутствует - берем как есть
    key: Callable = key if isinstance(key, Callable) else lambda k: k
    # извлекаем сортируемые данные
    result: list = [key(item) for item in iterable]

    for idx in range(1, len(result)):
        current: [int, float, str] = result[idx]
        position: int = idx

        # ищем позицию вставки с учетом направления и конца списка
        while cmp(result[position - 1], current) and position > 0:
            result[position] = result[position - 1]
            position -= 1

        result[position] = current

    return result


def my_abs(x: number_types) -> number_types:
    """ Возвращает число по модулю
    :param x: число
    :return: число по модулю
    """
    if isinstance(x, complex):
        return sqrt(x.real ** 2 + x.imag ** 2)

    return -x if x < 0 else x


def my_range(start: int, stop: int = None, step: int = 1) -> Iterable:
    """ Возвращает объект-генератор. Функция полностью эмулирует встроенный range
    но можно переделать, чтобы генерировались и дробные значения
    :param start: начальное значение (по умолчанию = 0)
    :param stop: конечное значение
    :param step: шаг (по умолчанию = 1)
    :return: генратор по параметрам
    """
    # базовые проверки
    if (
            not isinstance(start, int)
            or not (stop is None or isinstance(stop, int))
            or not (step is None or isinstance(step, int))
    ):
        raise TypeError(f"'{start.__class__.__name__}' "
                        f"object cannot be interpreted as an integer")

    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step


def my_pow(base: number_types, exp: number_types, mod: number_types = None) -> number_types:
    """ Функция возведения в степень, реализованная через while
    Если присутствует mod, то вычисляется pow(base, exp) % mod
    :param base: число возводимое в степень
    :param exp: показатель степени
    :param mod: остаток от деления на mod
    :return: base ** exp или (base ** exp) % mod
    """
    if not isinstance(base, number_types) or not isinstance(exp, number_types):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, number_types):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    if mod is not None and exp < 0:
        raise ValueError('base is not invertible for the given modulus')

    result = 1

    for _ in my_range(my_abs(exp)):
        result *= base

    result = 1 / result if exp < 0 else result

    if mod is None:
        return result
    else:
        return result % mod


def my_all(iterable: Iterable) -> bool:
    """ Аналог built in all функции
    :param iterable: проверяемый итерирруемый объект
    :return: True если все элементы iterable True, иначе False
    """
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{iterable.__class__.__name__}' object is not iterable")

    for item in iterable:
        if not item:
            return False

    return True


# print(my_sorted([1,4,3,2,5]))
# asd = min([])
#
# def my_min(iterable: Iterable, key: Callable = None, defalt=0):
#     if not isinstance(iterable, Iterable):
#         raise TypeError(f"'{iterable.__class__.__name__}' object is not iterable")
#
#     value = None
#
#     key_ = key if isinstance(key, Callable) else lambda x, y: x < y
#
#     for idx in range(len(iterable)):
#         if key_(iterable[idx], value):
#             value = iterable[idx]
#
#     return value
#
# def my_max(iterable: Iterable)
#     pass


if __name__ == '__main__':
    print('test 1 my_range ', list(my_range(0)) == list(range(0)) )
    print('test 2 my_range ', list(my_range(2)) == list(range(2)) )
    print('test 3 my_range ', list(my_range(1, 2)) == list(range(1, 2)) )
    print('test 4 my_range ', list(my_range(1, 4, 2)) == list(range(1, 4, 2)) )

    print('test 1 my_abs', my_abs(2) == 2)
    print('test 2 my_abs', my_abs(-2) == 2)
    print('test 3 my_abs', my_abs(complex(2.2)) == abs(complex(2.2)))

    print('test 1 my_pow', my_pow(2, 3) == pow(2, 3))
    print('test 2 my_pow', my_pow(2, -3) == pow(2, -3))
    print('test 3 my_pow', my_pow(2, 3, 6) == pow(2, 3, 6))
    try:
        my_pow(2, -3, 6)
    except ValueError as e:
        my_ex = e
    try:
        pow(2, -3, 6)
    except ValueError as e:
        bt_ex = e
    print('test 4 my_pow', type(my_ex) == type(bt_ex))
