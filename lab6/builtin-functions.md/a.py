def multiple (a ):
    b = 1
    for i in range(len(a)):
        b = b * a[i]
    return b
k = [1 , 2, 3 , 4 ,5 ,6]
print(multiple(k))
