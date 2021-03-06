def con(x):
    if x in 'ABC':return ord(x)-65
    return 3
from collections import deque
input=__import__('sys').stdin.readline
score=[[100,70,40,0],[70,50,30,0],[40,30,20,0],[0,0,0,0]]
dx,dy=[0,0,1,-1],[1,-1,0,0]
n=int(input())
nm=n**2+2
S=nm-2;E=S+1
c=[[0]*nm for _ in range(nm)]
d=[[0]*nm for _ in range(nm)]
f=[[0]*nm for _ in range(nm)]
path=[[] for _ in range(nm)]
D=[[*input()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        D[i][j]=con(D[i][j])
for i in range(n):
    for j in range(n):
        k=i*n+j
        if (i+j)%2==0:
            c[S][k]=1
            path[S].append(k)
            path[k].append(S)
            c[k][E]=1
            path[k].append(E)
            path[E].append(k)
            for z in range(4):
                nx,ny=i+dx[z],j+dy[z]
                nk=nx*n+ny
                if 0<=nx<n and 0<=ny<n:
                    c[k][nk]=1
                    path[k].append(nk)
                    path[nk].append(k)
                    d[k][nk]=-score[D[i][j]][D[nx][ny]]
                    d[nk][k]=-d[k][nk]
        else:
            c[k][E]=1
            path[k].append(E)
            path[E].append(k)
cost=0
while 1:
    q=deque([S])
    prev=[-1]*nm
    dist=[float('inf')]*nm
    inQ=[0]*nm
    dist[S]=0;inQ[S]=1
    while q:
        x=q.popleft()
        inQ[x]=0
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and dist[nx]>dist[x]+d[x][nx]:
                dist[nx]=dist[x]+d[x][nx]
                prev[nx]=x
                if inQ[nx]==0:q.append(nx);inQ[nx]=1
    if prev[E]==-1:break
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=1
        f[x][nx]-=1
        cost+=d[nx][x]
        x=nx
print(-cost)