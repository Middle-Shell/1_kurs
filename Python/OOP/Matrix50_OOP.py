class Matrix:

    count = 0
    def __init__(self):
        Matrix.count += 1
        self.matrixf = []
        print(Matrix.count)

    def input(self, mc, nc):
        self.matrixf = [[0 for _ in range(mc)] for _ in range(nc)]
        for i in range(nc):
            self.matrixf[i] = Column.inputC(mc)

    def output(self):
        for row in self.matrixf:
            for x in row:
                print("{:4d}".format(x), end="")
            print()


class Column:

    def inputC(ms):
        return list(map(int, input("Enter " + str(ms) + " numbers through space: ").split()))

    def exchange(matrixc, ns):
        for j in range(ns):
            mi = min(matrixc[j])
            ma = max(matrixc[j])
            mii = matrixc[j].index(mi)
            mai = matrixc[j].index(ma)

            matrixc[j][mii] = ma
            matrixc[j][mai] = mi
        return matrixc


m, n = map(int, input("Enter m and n through space: ").split())
matrixL = Matrix()
matrixL.input(m, n)
matrixL.matrixf = Column.exchange(matrixL.matrixf, n)
matrixL.output()

m, n = map(int, input("Enter m and n through space: ").split())
matrixZ = Matrix()
matrixZ.input(m, n)
matrixZ.matrixf = Column.exchange(matrixZ.matrixf, n)
matrixZ.output()
#Дана матрица размера M × N. Преобразовать матрицу, поменяв
#местами минимальный и максимальный элемент в каждом столбце.