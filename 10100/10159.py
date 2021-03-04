n=int(input())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
K=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(int(input())):
    a,b=map(int,input().split())
    S[a][b]=1;K[b][a]=1
for i in range(1,n+1):
    S[i][i]=1;K[i][i]=1
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
            K[i][j]=min(K[i][j],K[i][k]+K[k][j])
D=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    D[i][0]=0
    for j in range(1,n+1):
        if S[i][j]==float('inf')==K[i][j]:D[i][j]=1
        else:D[i][j]=0
for i in range(1,n+1):
    print(sum(D[i]))