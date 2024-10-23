a = []
for i in range(1, 11):
    a.append(i)
b = []
for i in range(11, 21):
    b.append(i)
c = []
for i in range(21, 31):
    c.append(i)
def pr(a):
    s = 1
    for i in range(len(a)):
        s *= a[i]
    return s
def sa(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s//len(a)
print("исходные массивы: ", a, b, c)
print("произведение элементов: ", pr(a), pr(b), pr(c))
print("среднее арифметическое: ", sa(a), sa(b), sa(c))