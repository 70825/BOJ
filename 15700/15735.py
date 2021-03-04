n = int(input())
if 1<=n<=10000:
    if n % 2 == 0:
        print(int((n*(n+2)*(2*n+1)/8)))
    else:
        print(int((n+1)*(2*n**2+3*n-1)/8))