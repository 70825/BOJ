n,m=map(int,input().split())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    S[a][b]=c
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[k][j]+S[i][k])
ans=float('inf')
for i in range(n+1):
    ans=min(ans,S[i][i])
print([ans,-1][ans==float('inf')])