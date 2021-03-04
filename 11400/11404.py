input=__import__('sys').stdin.readline
n=int(input())
m=int(input())
cost=[[float('inf')]*n for _ in range(n)]
for i in range(n):
    cost[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    cost[a][b]=min(cost[a][b],c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
for i in range(n):
    for j in range(n):
        if cost[i][j]==float('inf'):print(0,end=' ')
        else:print(cost[i][j],end=' ')
    print()