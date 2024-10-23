a = int(input())
b = int(input())
while a < b:
    print(a, end=" ")
    a = a + 1
while a > b:
    print(b, end=" ")
    b = b + 1
print(b)