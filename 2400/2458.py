input=__import__('sys').stdin.readline
n,m=map(int,input().split())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    S[a][b]=1
for i in range(1,n+1):
    S[i][i]=1
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
ans=0
for i in range(1,n+1):
    t=1
    for j in range(1,n+1):
        if S[i][j]==S[j][i]==float('inf'):t=0
    if t:ans+=1
print(ans)