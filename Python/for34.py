n = int(input())
a = 1
b = 2
for i in range(3, n+1):
    c = (a+2*b)/3
    a = b
    b = c
    print(c)