from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
C=[[0]*n for _ in range(n)]
F=[[0]*n for _ in range(n)]
path=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    C[a][b]+=1
    path[a].append(b)
    path[b].append(a)
S,E=0,1
res=0
while 1:
    q=deque([S])
    prev=[-1]*n
    visited=[0]*n
    visited[S]=1
    while q:
        x=q.popleft()
        for nx in path[x]:
            if C[x][nx]-F[x][nx]>0 and not visited[nx]:
                visited[nx]=1;prev[nx]=x;q.append(nx)
    if not visited[E]:break
    x=E
    while x!=S:
        F[prev[x]][x]+=1
        F[x][prev[x]]-=1
        x=prev[x]
    res+=1
print(res)