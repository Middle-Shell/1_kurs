
n = int(input('Enter N = '))
a = list(map(int, input("Enter through space N numbers ").split()))
k = True
for i in range(n-1):
    if a[i+1] <= a[i]:
        k = False
        break
print(k)