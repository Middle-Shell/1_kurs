def AddLeftDigit(d, k):
    p = d
    m = 1
    if k < 0:
        m = -1
    elif k == 0:
        print(d)
        return(d)
    while d > 0:
        d //= 10
        k *= 10
    p = k + p * m
    print(p)
    return p

d = AddLeftDigit(int(input("Enter digital: ")), int(input("Enter left digital: ")))
d = AddLeftDigit(d, int(input("Enter left digital: ")))