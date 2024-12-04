import random #генерация случайных чисел
pol = 0#переменная для подсчета
a=0#для суммы
b=0#для матрицы
k=1
r = []#создаем массив
N=int(input('Ввод: '))#ввод числа ,размер матрицы
A=[[random.randrange(10) for b in range(N)] for j in range(N)]# Создает квадратную матрицу со случайными числами от 0 до 9.
for row in range(N):#внешний цикл ,перебор строки матрицы
    for col in range(row + 1, N):#внутрений цикл , перебор столбцов
         a+=A[row][col]

for row in range(N):#подсчет положительных элементов
    r.append(input())
    if N > 0:
        pol += 1#подсчет строк
print('Сумма:', a)
print('Число:', pol)