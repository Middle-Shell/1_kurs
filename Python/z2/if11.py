a = int(input("a = "))
b = int(input("b = "))
if a > b:
    b = a
elif a < b:
    a = b
else:
    a, b = 0, 0
print('a = ', a,' b = ', b)