N,M=map(int,input().split())
a=[0]*M
c=[False]*(N+1)
def go(index,start,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    for i in range(start,n+1):
        c[i]=True;a[index]=i
        go(index+1,i,n,m)
        c[i]=False
go(0,1,N,M)