n = int(input("Enter n: "))
fprog = list(map(int, input("Enter numbers separated by space: ").split()))
sprog = []
sumd = 0
for k in range(n):
    sumd += fprog[k]
    sprog.append(sumd)
for raw in sprog:
    print(raw)
#Дан массив A размера N. Сформировать новый массив B того же
#размера по следующему правилу: элемент BK равен сумме элементов
#массива A с номерами от 1 до K