input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[float('inf')]*n for _ in range(n)]
for i in range(n):D[i][i]=0
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    D[a][b]=1;D[b][a]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
ans=float('inf')
res=0
for i in range(n):
    k=sum(D[i])
    if ans>k:ans=k;res=i
print(res+1)