"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из
слов, разделенных пробелом. Каждое слово состоит из латинских букв в
нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее
функцию int_func().
"""

from sys import argv


def int_func(word: str) -> str:
    """
    Переводит первый символ слова в верхний регистр
    :param word: слово для преобразования
    :return: преобразованное слово
    """
    if not word.isascii() and not word.isalpha():
        raise ValueError(f'Слово {word} содержит не ASCII символы, или латинские символы')

    if not word.islower():
        raise ValueError(f'Слово {word} содержит не только строчные символы')

    return word.title()


def run_help():
    print(f"Usage: python3 {argv[0]} 'word1 word2'")
    exit(0)


if __name__ == '__main__':
    try:
        words = argv[1].split()
        if len(words) < 2:
            raise RuntimeError()
    except (IndexError, RuntimeError):
        print('Неверный параметр запучска')
        run_help()

    print(' '.join([int_func(item) for item in words]))
