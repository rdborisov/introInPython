# 3. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def subsequence(num):
    result = (1 + 1 / num) ** num
    return result


def main(n, amount=0):
    if is_int(n):
        for i in range(int(n)):
            print("%.2f" % subsequence(i + 1), end=" ")
            amount += subsequence(i + 1)
        print()
        print("SUM: ""%.2f" % amount)

    else:
        print("Wrong number")


n = input("Input N: ")
main(n)
