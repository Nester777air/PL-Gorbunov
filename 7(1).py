a = int(input("число a: "))
c = 0
def s(n):
    return sum(int(d) for d in str(n))

while a > 0:
    a -= s(a)
    if a > 0:
        c += 1
print("кол-во действий:", c+1)