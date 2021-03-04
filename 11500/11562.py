n,m=map(int,input().split())
input=__import__('sys').stdin.readline
D=[[] for _ in range(n+1)]
S=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    if c==0:
        D[a].append((b,0))
        D[b].append((a,1))
        S[a][b]=0;S[b][a]=1
    else:
        D[a].append((b,0))
        D[b].append((a,0))
        S[a][b]=0;S[b][a]=0
for i in range(1,n+1):
    S[i][i]=0
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(S[a][b])