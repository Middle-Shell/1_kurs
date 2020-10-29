def arifprog(a, d, n):
    prog = []
    for i in range(n):
        prog.append(a + (d * i))
    return prog
prog = arifprog(float(input("Enter first term: ")), float(input("Enter residul: ")), int(input("Enter n: ")))
for ind in prog:
    print(ind)