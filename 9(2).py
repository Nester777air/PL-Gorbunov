def f(n,k):#найти ближайшее к n число начиная с к
    if n>k:
        print(k)#выводим текущее значение k
        return f(n,k+1)#вызываем функцию увелич k на 1 ,к n
    if n<k:
        print(k)# выводим значение k так как оно больше n
        return f(n,k-1)#уменьшаем к на 1
    if n==k:
        return k# функция возвращает к так как равны
a=int(input())
b=int(input())
print(f(a,b))