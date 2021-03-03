from collections import deque
input=__import__('sys').stdin.readline
n,k,d=map(int,input().split())
c=[[0]*(n+d+2) for _ in range(n+d+2)]
f=[[0]*(n+d+2) for _ in range(n+d+2)]
path=[[] for _ in range(n+d+2)]
S=n+d;E=S+1
for i in range(n):
    c[S][i]=k
    path[S].append(i)
    path[i].append(S)
D=[*map(int,input().split())]
for i in range(d):
    c[n+i][E]=D[i]
    path[n+i].append(E)
    path[E].append(n+i)
for i in range(n):
    a,*b=map(int,input().split())
    for j in b:
        c[i][j-1+n]=1
        path[i].append(j-1+n)
        path[j-1+n].append(i)
res=0
while 1:
    q=deque([S])
    prev=[-1]*(n+d+2)
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                prev[nx]=x;q.append(nx)
    if prev[E]==-1:break
    flow=float('inf')
    x=E
    while x!=S:
        nx=prev[x]
        flow=min(flow,c[nx][x]-f[nx][x])
        x=nx
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=flow
        f[x][nx]-=flow
        x=nx
    res+=flow
print(res)