n=int(input('введите длину массива'))
array=[]
print('введите элементы массива')
for i in range (n):
    element=int(input(f"элемент{i+1}:"))
    array.append(element)
max_element=array[0]
for num in array :
    if num> max_element:
        max_element=num
print("максимальный элемент массива:", max_element)
