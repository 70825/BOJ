from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
max_n=100
max_v=2*(max_n+1)
S=max_v-2
E=max_v-1
c=[[0]*max_v for _ in range(max_v)]
d=[[0]*max_v for _ in range(max_v)]
f=[[0]*max_v for _ in range(max_v)]
path=[[] for _ in range(max_v)]
A=[*map(int,input().split())]
for i in range(max_n,max_n+n):
    c[i][E]=A[i-max_n]
    path[i].append(E)
    path[E].append(i)
B=[*map(int,input().split())]
for i in range(m):
    c[S][i]=B[i]
    path[S].append(i)
    path[i].append(S)
D=[[*map(int,input().split())] for _ in range(m)]
for i in range(m):
    for j in range(max_n,max_n+n):
        d[i][j]=D[i][j-max_n]
        d[j][i]=-d[i][j]
        c[i][j]=float('inf')
        path[i].append(j)
        path[j].append(i)
res=0
while 1:
    q=deque([S])
    prev=[-1]*max_v
    dist=[float('inf')]*max_v
    dist[S]=0
    inQ=[0]*max_v
    inQ[S]=1
    while q:
        x=q.popleft()
        inQ[x]=0
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and dist[nx]>dist[x]+d[x][nx]:
                dist[nx]=dist[x]+d[x][nx]
                prev[nx]=x
                if inQ[nx]==0:
                    q.append(nx)
                    inQ[nx]=1
    if prev[E]==-1:break
    flow=float('inf')
    x=E
    while x!=S:
        flow=min(flow,c[prev[x]][x]-f[prev[x]][x])
        x=prev[x]
    x=E
    while x!=S:
        res+=flow*d[prev[x]][x]
        f[prev[x]][x]+=flow
        f[x][prev[x]]-=flow
        x=prev[x]
print(res)