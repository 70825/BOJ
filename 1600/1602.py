input=__import__('sys').stdin.readline
n,m,q=map(int,input().split())
T=[*map(int,input().split())]
Sort=[]
for i in range(n):Sort.append([T[i],i])
D=[[float('inf')]*n for _ in range(n)]
cost=[[float('inf')]*n for _ in range(n)]
for i in range(n):D[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    D[a][b]=min(D[a][b],c)
    D[b][a]=min(D[b][a],c)
Sort=sorted(Sort)
for k in range(n):
    t=Sort[k][1]
    for i in range(n):
        for j in range(n):
            D[i][j]=min(D[i][j],D[i][t]+D[t][j])
            cost[i][j]=min(cost[i][j],D[i][j]+max(T[i],T[j],T[t]))
for i in range(q):
    a,b=map(int,input().split())
    a-=1;b-=1
    print([cost[a][b],-1][cost[a][b]==float('inf')])