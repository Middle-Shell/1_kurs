n = int(input())
a = 1
b = 2
for i in range(3, n+1):
    c = (a+2*b)/3
    a = b
    b = c
    print(c)
#Дано целое число N (> 1). Последовательность вещественных чисел AK
#определяется следующим образом:
#A1 = 1, A2 = 2, AK = (AK−2 + 2·AK−1)/3, K = 3, 4, . . . .
#Вывести элементы A1, A2, . . . , AN .