x, y = map(int, input("Enter x/y through  space ").split())
if x == y:
    print(0)
elif y == 0:
    print(1)
elif x == 0:
    print(2)
else:
    print(3)