import random #генерация случайных чисел
a = int(input())
b = int(input())
B = [[random.randrange(10) for i in range(a)] for j in range(a)]
for i in range(a, b):
    if B[i][j] >= 0:
        print('Максимальный элемент:')
    if B[i][j] < 0:
        print('Минимальный элемент:')
