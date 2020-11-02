m, n, d = map(int, input("Enter m and n through space: ").split())
matrixM = [[0 for _ in range(m)] for _ in range(n)]
matrixM[0] = list(map(int, input("Enter " + str(m) + " numbers through space: ").split()))
for i in range(1, n):
    for j in range(m):
        matrixM[i][j] = matrixM[i-1][j] + d
for i in range(n):
    print("********************")
    for j in range(m):
        print(matrixM[i][j])
#Даны целые положительные числа M, N, число D и набор из M чисел. Сформировать матрицу размера M × N, у которой первый столбец
#совпадает с исходным набором чисел, а элементы каждого следующего
#столбца равны сумме соответствующего элемента предыдущего столбца
#и числа D (в результате каждая строка матрицы будет содержать элементы
#арифметической прогрессии).
