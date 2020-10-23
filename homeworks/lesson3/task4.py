"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в
виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая
использование цикла.
"""

numeric = (int, float, complex)


def my_pow1(base: numeric, exp: numeric, mod: numeric = None) -> numeric:
    """
    Функция возведения в степень реализованная через **
    Если присутствует mod, то вычисляется pow(base, exp) % mod
    :param base: число возводимое в степень
    :param exp: показатель степени
    :param mod: остаток от деления на mod
    :return: base ** exp или (base ** exp) % mod
    """
    if not isinstance(base, numeric) or not isinstance(exp, numeric):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, numeric):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    result = base ** exp

    if mod is None:
        return result
    else:
        return result % mod


def my_pow2(base: numeric, exp: numeric, mod: numeric = None) -> numeric:
    """
    Функция возведения в степень, реализованная через while
    Если присутствует mod, то вычисляется pow(base, exp) % mod
    :param base: число возводимое в степень
    :param exp: показатель степени
    :param mod: остаток от деления на mod
    :return: base ** exp или (base ** exp) % mod
    """
    if not isinstance(base, numeric) or not isinstance(exp, numeric):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, numeric):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    result = 1

    while exp:
        result *= base
        exp -= 1

    if mod is None:
        return result
    else:
        return result % mod


if __name__ == '__main__':
    print(my_pow1(3, 4))
    print(my_pow2(3, 6, 4))

