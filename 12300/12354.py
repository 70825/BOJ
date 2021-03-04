for _ in range(int(input())):
    n=int(input())
    A=[*map(int,input().split())]
    D=[1]*n
    for i in range(n):
        for j in range(i):
            if A[i]>A[j]:D[i]=max(D[i],D[j]+1)
    print('Case #{}: {}'.format(_+1,n-max(D)))