"""
Пользователь вводит целое положительное число. Найдите самую
большую цифру в числе. Для решения используйте цикл while и
арифметические операции.
"""

digits = list(input('Please enter integer minimum 2 sign: '))

compare = lambda x, y: int(x) >= int(y)

while len(digits) > 1:
   _ = digits.pop(1) if compare(digits[0], digits[1]) else digits.pop(0)

print(f'Maximum digit is {digits[0]}')
