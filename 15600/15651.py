N,M=map(int,input().split())
c=[False]*(N+1)
a=[0]*M
def go(index,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    for i in range(1,n+1):
        a[index]=i
        go(index+1,n,m)
go(0,N,M)