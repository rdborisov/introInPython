# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_weekend(num):
    if is_int(num):
        if (int(num) >= 6 and int(num) <= 7):
            print(f"{int(num)} -> Да")
        else:
            print(f"{int(num)} -> Нет")
    else:
        print("Введите число!")

def main():
    num = input("Input Num: ")
    is_weekend(num)

main()