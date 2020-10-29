"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников.
"""
import sys


MINIMAL_SALARY = 20000
FILENAME = "task3.txt"

try:
    with open(FILENAME, encoding='utf-8') as fh:
        employees = fh.readlines()
except IOError as e:
    print(e)
    sys.exit(1)

summ_salary = 0

for employee in employees:
    name, salary = employee.split()

    try:
        salary = float(salary)
    except ValueError:
        continue

    summ_salary += salary
    if salary < MINIMAL_SALARY:
        print(name)

print('Average salary: ', round(summ_salary / len(employees), 2))