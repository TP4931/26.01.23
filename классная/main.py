a = [2, 3, 4, 5]
b = [0] * 20

a[2] = 8
a[-1] = 10

a.append(20)
print(a)
print(len(a))
print(max(a), min(a))

for i in range(len(a)):
    print(i, a[i], a[i] % 2 == 0)

