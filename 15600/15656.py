N,M=map(int,input().split())
a=[0]*M
c=[False]*N
D=sorted([*map(int,input().split())])
def go(index,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    for i in range(n):
        c[i]=True;a[index]=D[i]
        go(index+1,n,m)
        c[i]=False
go(0,N,M)