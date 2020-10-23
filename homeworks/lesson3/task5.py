"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""

# эта библиотечная функция позволяет обрабатывать
# hax, bin, oct, int, float и complex числа
# from ast import literal_eval

from my_functions import my_sum

stop_index = None
result = 0


def convert_item(item: str) -> (int, float):
    """
    Преобразование строки в число
    :param item: строковое представление числа
    :return: число
    """
    try:
        float_item = float(item)
        int_item = int(item.split('.')[0])
    except ValueError:
        raise

    if float_item == int_item:
        return int_item
    else:
        return float_item


if __name__ == '__main__':
    while stop_index is None:
        data = input('Пожалуйста введите числа разделённые\n'
                     'пробелами (допускаются int, float): ').split()

        try:
            stop_index = data.index('q')
            data = data[:stop_index]
        except ValueError:
            pass

        try:
            data = [convert_item(i) for i in data]
        except ValueError:
            print("Введенные данные содержат неверный тип")
            continue

        result += my_sum(data)

        print(result)

