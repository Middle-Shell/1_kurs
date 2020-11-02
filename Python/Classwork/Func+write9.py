def even():
    a = list(map(int, open('input.txt', 'r').read().split()))
    k = 0
    f = open('output.txt', 'w')
    f.write('odd index: ' + '\n')
    for i in range(len(a)):
        if a[i]%2 != 0:
            print(i)
            f.write(str(i) + '\n')
            k += 1
    f.write('Total: ' + str(k))
    f.close()
even()
#write9 но с получением данных из файла и вывод в файл