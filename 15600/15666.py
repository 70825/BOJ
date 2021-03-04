N,M=map(int,input().split())
a=[0]*M
c=[False]*N
D=sorted([*(map(int,input().split()))])
memo=[]
def go(index,start,n,m):
    if index==m:
        memo.append(tuple(a))
        return
    for i in range(start,n):
        c[i]=True;a[index]=D[i]
        go(index+1,i,n,m)
        c[i]=False
go(0,0,N,M)
memo=sorted(list(set(memo)))
for k in memo:
    print(' '.join(map(str,k)))