# n - сколько нужно добавить элементов в массив
# (0, 1, ... , n) числа, которыми заполнится массив
n = int(input())
# t = int(input()) # с к числа
x = []
for i in range(n):
    w = int(input())
    if w%2==0:
        x.append(w)
print(x)