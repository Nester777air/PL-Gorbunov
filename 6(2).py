n=int(input('введите длину массива'))
array=[]
print('введите элементы массива:')
for i in range(n):
    element=float(input(f'элемент{i+1}:'))
    array.append(element)
average=sum(array)/n
for i in range(n):
    if array[i]==0:
        array[i]=average
print('измененный массив:',array)