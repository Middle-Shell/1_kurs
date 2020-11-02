m, n = map(int, input("Enter m and n through space: ").split())
matrixM = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    matrixM[i] = list(map(int, input("Enter " + str(m) + " numbers through space: ").split()))
for i in range(n):
    mi = min(matrixM[i])
    ma = max(matrixM[i])
    mii = matrixM[i].index(min(matrixM[i]))
    mai = matrixM[i].index(max(matrixM[i]))

    matrixM[i][mii] = ma
    matrixM[i][mai] = mi
for i in range(n):
    print("*****************************")
    for j in range(m):
        print(matrixM[i][j])
#Дана матрица размера M × N. Преобразовать матрицу, поменяв
#местами минимальный и максимальный элемент в каждом столбце.
