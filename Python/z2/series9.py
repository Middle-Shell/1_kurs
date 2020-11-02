n = int(input('Enter N = '))
a = list(map(int, input("Enter through space N numbers ").split()))
k = 0
for i in range(n):
    if a[i]%2 != 0:
        print(i)
        k += 1
print('Total:', k)
#Дано целое число N и набор из N целых чисел. Вывести в том же
#порядке номера всех нечетных чисел из данного набора и количество K
#таких чисел