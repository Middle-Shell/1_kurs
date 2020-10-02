def even():
  a = list(map(int, input("Enter N numbers through space ").split()))
  k = 0
  for i in range(len(a)):
    if a[i]%2 != 0:
      print(i)
      k += 1
  print('Total:', k)

even()