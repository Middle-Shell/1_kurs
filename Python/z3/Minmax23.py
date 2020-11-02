n = int(input("Enter n(>3): "))
dig = list(map(int, input("Enter " + str(n) + " numbers separated by space: ").split()))
max = [0, 0, 0]
for i in range(n):
    if dig[i] > max[0]:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = dig[i]
for i in range(3):
    print("Max" + str(i+1) + " = " + str(max[i]))
#Дано целое число N (> 3) и набор из N чисел. Найти три наибольших элемента из данного набора и вывести эти элементы в порядке
#убывания их значений.
