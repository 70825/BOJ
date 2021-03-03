n = int(input())
a = [0,1]
if n in [0,1]:print(a[n])
else:
    for i in range(n-1):
        a[0],a[1] = a[1],a[0]+a[1]
    print(a[1])