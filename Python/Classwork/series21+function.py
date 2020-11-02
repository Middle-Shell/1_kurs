def uneven():
	a = list(map(int, input("Enter through space N numbers ").split()))
	k = True
	for i in range(len(a)-1):
		if a[i+1] <= a[i]:
			k = False
			break
	print(k)
	
uneven()
#series21 но через функцию