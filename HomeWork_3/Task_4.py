# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = 45
n = num
s = ''
while num != 0:
    s = str(num % 2) + s
    num //= 2
print(n, '->', s)
