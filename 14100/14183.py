while 1:
    n,m=map(int,input().split())
    if n==m==0:break
    A=[*map(int,input().split())]
    k=0
    for i in range(m):
        B=[*map(int,input().split())]
        for j in range(n):
            if A[j]<B[j]:k+=1;break
    print(m-k)