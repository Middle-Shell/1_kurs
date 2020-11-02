def uneven():
	a = list(map(int, open('input.txt', 'r').read().split()))
	k = True
	f = open('output.txt', 'w')
	for i in range(len(a)-1):
		if a[i+1] <= a[i]:
			k = False
			break
	f.write(str(k))
	f.close()
	
uneven()
#write21 но с получением данных из файла и вывод в файл