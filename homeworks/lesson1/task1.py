
"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите
у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

user_name = 'test user'
user_message = 'message undefined'
count = 1

print(f'({count}) Привет! Я {user_name}. Моё сообщение "{user_message}"')

user_name = input('Введите свое имя: ')
user_message = input('Введите свое сообщение: ')
count += 1

print(f'({count}) Привет {user_name}! Принимаю сообщение "{user_message}"')
