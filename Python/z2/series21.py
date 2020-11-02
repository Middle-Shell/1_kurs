
n = int(input('Enter N = '))
a = list(map(int, input("Enter through space N numbers ").split()))
k = True
for i in range(n-1):
    if a[i+1] <= a[i]:
        k = False
        break
print(k)
#Дано целое число N (> 1) и набор из N вещественных чисел. Проверить, образует ли данный набор возрастающую последовательность. Если
#образует, то вывести TRUE, если нет — вывести FALSE.