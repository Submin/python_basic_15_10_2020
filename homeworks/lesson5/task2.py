"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

filename = "task2.txt"

with open(filename, 'r', encoding='utf-8') as file:
    lines = [line for line in file.readlines() if line != '\n']

    print(f"В файле непустых строк:", len(lines))

    for line, words_cnt in {l: len(l.split()) for l in lines}.items():
        print(f'Строка {line[:50]}... содержит {words_cnt} слов')
