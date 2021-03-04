from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
c=[[0]*(n+m+2) for _ in range(n+m+2)]
f=[[0]*(n+m+2) for _ in range(n+m+2)]
path=[[] for _ in range(n+m+2)]
S=n+m;E=S+1
A=[*map(int,input().split())]
for i in range(n):
    c[i+m][E]=A[i]
    path[i+m].append(E)
    path[E].append(i+m)
B=[*map(int,input().split())]
for i in range(m):
    c[S][i]=B[i]
    path[i].append(S)
    path[S].append(i)
C=[[*map(int,input().split())] for _ in range(m)]
for i in range(m):
    for j in range(n):
        c[i][j+m]=C[i][j]
        path[j+m].append(i)
        path[i].append(j+m)
res=0
while 1:
    q=deque([S])
    prev=[-1]*(n+m+2)
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