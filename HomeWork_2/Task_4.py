# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


n = 5
list = []
res = []
data = open('file.txt', 'r')
with open("file.txt", "r") as file:
    for line in file:
        j = 0
        for i in range(-n, n + 1):
            list.insert(j, i)
            res.insert(j, list)
            j += 1
print(list)
print(res)

data.close()