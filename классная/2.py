# Создать массив и добавить в него нечётные элемент с 1 до n. при n = 7 [1, 3, 5, 7]
# n - поступает на вход программы
x=[]
n= int(input())
for i in range(1, n+1):
    if i % 2 != 0:
        x.append(i)
print(x)

# x=[]
# n= int(input())
# for i in range(1, n+1, 2):
#     x.append(i)
# print(x)
