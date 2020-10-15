"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

convert = lambda x, n: int(str(x) * n)

num = int(input('Please enter number: '))
print(num + convert(num, 2) + convert(num, 3))
