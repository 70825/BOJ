def edge(x,y,z):
    path[x].append(y)
    path[y].append(x)
    c[x][y]=z
def bfs():
    global level
    level=[-1]*nm
    level[S]=0
    q=deque([S])
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and level[nx]==-1:
                level[nx]=level[x]+1;q.append(nx)
    return level[E]>0
def dfs(x,end,flow):
    if x==end:return flow
    while work[x]<len(path[x]):
        nx=path[x][work[x]]
        if c[x][nx]-f[x][nx]>0 and level[nx]==level[x]+1:
            df = dfs(nx,end,min(c[x][nx]-f[x][nx],flow))
            if df>0:
                f[x][nx]+=df
                f[nx][x]-=df
                return df
        work[x]+=1
    return 0
from collections import deque
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n=int(input())
    nm=2*(n+1)
    S=nm-2;E=S+1
    soldier=0
    c=[[0]*nm for _ in range(nm)]
    path=[[] for _ in range(nm)]
    enemy=[0]*n
    D=[*map(int,input().split())]
    for i in range(n):
        if D[i]>0:
            edge(S,i,D[i])
            edge(i+n,E,1)
            edge(i,i+n,100000)
            soldier+=1
    for i in range(n):
        K=input()
        if D[i]!=0:
            for j in range(len(K)):
                if K[j]=='Y':
                    if D[j]!=0:edge(i,n+j,100000)
                    else:enemy[i]=1
    l,r=0,sum(D)+1
    res=0
    while l<=r:
        m=(l+r)//2
        f=[[0]*nm for _ in range(nm)]
        for i in range(n):
            if enemy[i]==1:c[i+n][E]=m
            if enemy[i]==0 and D[i]>0:c[i+n][E]=1
        ALL=soldier-sum(enemy)+sum(enemy)*m
        ans=0
        level=[-1]*nm
        while bfs():
            work=[0]*nm
            while 1:
                flow=dfs(S,E,float('inf'))
                if flow==0:break
                ans+=flow
        if ans==ALL:l=m+1;res=max(res,m)
        else:r=m-1
    print(res)