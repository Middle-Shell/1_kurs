n = int(input())
t = False
while n != 0:
    bal = n % 10
    if bal % 2 != 0:
        t = True
        break
    n //= 10
print(t)