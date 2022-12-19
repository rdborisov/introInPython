# * Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def is_int(Num):
    try:
        int(Num)
        return True
    except ValueError:
        return False

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

def factorialSequence(n):
    if is_int(n):
        for i in range(int(n)):
            print(fac(i+1), end=" ")
    else:
        print("Wrong number")

factorialSequence(input("Input number: "))