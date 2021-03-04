def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            P[x]=nx
            B[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,m=map(int,input().split())
    path=[[] for _ in range(m)]
    for i in range(m):
        a,b=map(int,input().split());a-=1
        for j in range(a,b):
            path[i].append(j)
    P=[-1]*m
    B=[-1]*n
    res=0
    for i in range(m):
        if P[i]==-1:
            visited=[0]*m
            if dfs(i):res+=1
    print(res)