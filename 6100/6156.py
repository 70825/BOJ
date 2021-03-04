n,m=map(int,input().split())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
K=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    S[i][i]=0
for i in range(m):
    a,b=map(int,input().split())
    S[a][b]=1;K[b][a]=1
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
            K[i][j]=min(K[i][j],K[i][k]+K[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        S[i][j]=min(S[i][j],K[i][j])
ans=0
for i in range(1,n+1):
    if sum(S[i][1:])!=float('inf'):ans+=1
print(ans)