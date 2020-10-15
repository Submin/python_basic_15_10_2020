"""
Пользователь вводит время в секундах. Переведите время в часы, минуты
 и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

num_seconds = int(input('Please enter seconds: '))

hours, secs_tail = divmod(num_seconds, 60 * 60)
minutes, seconds = divmod(secs_tail, 60)

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))