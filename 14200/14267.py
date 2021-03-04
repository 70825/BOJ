import sys
sys.setrecursionlimit(100001)
input=__import__('sys').stdin.readline
def dfs(x):
    for nx in P[x]:
        cost[nx]+=cost[x]
        dfs(nx)
n,m=map(int,input().split())
D=[*map(int,input().split())]
P=[[] for _ in range(n)]
cost=[0]*(n)
for i in range(1,n):
    P[D[i]-1].append(i)
for i in range(m):
    a,b=map(int,input().split())
    cost[a-1]+=b
dfs(0)
print(*cost)