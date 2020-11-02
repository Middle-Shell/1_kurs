arr = [1, 2, [3, 4, [1, 2, 3, 4,[1, 2, 3], 5, 6], 7, 8], 9, 9]

def rec(mas):
    for i in range(len(mas)):
        if type(mas[i]) is int:
            print(mas[i])
        else:
            rec(mas[i])
rec(arr)
#рекурсивная функция для вывода чисел из списка(аля каталоги и файлы)