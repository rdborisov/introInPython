# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).

quarter = int(input("quarter: "))

if (quarter != 0):
    if (quarter == 1):
        print(f'x > 0 and y > 0')
    elif (quarter == 2):
        print(f'x < 0 and y > 0')
    elif (quarter == 3):
        print(f'x < 0 and y < 0')
    elif (quarter == 4):
        print(f'x > 0 and y < 0')
else:
    print("y == 0 and x == 0")