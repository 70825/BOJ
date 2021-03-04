from decimal import Decimal
for _ in range(int(input())):
    n=int(input())
    D=[*map(int,input().split())]
    for i in range(1,n-1):
        k=Decimal((D[i-1]+D[i+1])/2)
        if D[i]>k:D[i]=k
    print('Case #{}: {}'.format(_+1,D[n-2]))