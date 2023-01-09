# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

length_list = random.randint(1, 10)
list = random.sample(range(10), length_list)
sum = 0
odd_list = []
for i in range(1, length_list, 2):
    odd_list.append(list[i])
    sum += list[i]

print(list, ' ->', odd_list, f'сумма: {sum}')
