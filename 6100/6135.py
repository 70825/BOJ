input=__import__('sys').stdin.readline
n,m,t=map(int,input().split())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    S[a][b]=c
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],max(S[i][k],S[k][j]))
for i in range(t):
    a,b=map(int,input().split())
    print([S[a][b],-1][S[a][b]==float('inf')])