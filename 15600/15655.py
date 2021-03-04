N,M=map(int,input().split())
a=[0]*M
c=[False]*N
D=sorted([*map(int,input().split())])
def go(index,start,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    for i in range(start,n):
        if c[i]:continue
        c[i]=True;a[index]=D[i]
        go(index+1,i+1,n,m)
        c[i]=False
go(0,0,N,M)