def arifprog(a, d, n):
    prog = []
    for i in range(n):
        prog.append(a + (d * i))
    return prog
prog = arifprog(float(input("Enter first term: ")), float(input("Enter residul: ")), int(input("Enter n: ")))
for ind in prog:
    print(ind)
#Дано целое число N (> 1), а также первый член A и разность D арифметической прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов данной прогрессии:
#A, A + D, A + 2·D, A + 3·D, .