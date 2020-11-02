n = int(input("Enter n: "))
dig = list(map(int, input("Enter numbers separated by space: ").split()))
min, mini = dig[0], 0
max, maxi = dig[0], 0
for i in range(n):
    if dig[i] < min:
        min = dig[i]
        mini = i
    if dig[i] >= max:
        max = dig[i]
        maxi = i
print(str(min) + ' ' + str(mini + 1))
print(str(max) + ' ' + str(maxi + 1))
#Дано целое число N и набор из N целых чисел. Найти номера
#первого минимального и последнего максимального элемента из данного
#набора и вывести их в указанном порядке