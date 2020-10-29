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