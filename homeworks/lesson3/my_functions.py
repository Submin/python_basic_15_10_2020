from typing import Iterable, Callable

number_types = (int, float, complex)


def my_div(x: number_types, y: number_types) -> number_types:
    """
    Делит число на число
    :param x: Делимое
    :param y: Делитель
    :return: Частное
    """
    if not (isinstance(x, number_types) and isinstance(y, number_types)):
        raise TypeError(f"unsupported operand type(s) for my_div: "
                        f"'{x.__class__.__name__}' and '{y.__class__.__name__}'")

    return x / y


def my_sum(iterable: Iterable, start: number_types = 0) -> [int, float]:
    """
    Возвращает сумму элементов iterable и statrt.
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


def my_sorted(iterable: Iterable, key: Callable = None, reverse: bool = False,) -> list:
    """
    Функция сортировки реализованная на алгоритме вставки а
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

# def my_all(iterable: Iterable):

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
