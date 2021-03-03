from collections import deque
input=__import__('sys').stdin.readline
n,p=map(int,input().split())
c=[[0]*(2*n) for _ in range(2*n)]
f=[[0]*(2*n) for _ in range(2*n)]
path=[[] for _ in range(2*n)]
for i in range(p):
    a,b=map(int,input().split())
    a=(a-1)*2+1
    b=(b-1)*2
    c[a][b]=1
    path[a].append(b)
    path[b].append(a)
    c[b+1][a-1]=1
    path[b+1].append(a-1)
    path[a-1].append(b+1)
for i in range(n):
    a,b=i*2,i*2+1
    c[a][b]=1
    path[a].append(b)
    path[b].append(a)
S,E=1,2
res=0
while 1:
    q=deque([S])
    prev=[-1]*(2*n)
    ans=0
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                prev[nx]=x;q.append(nx)
    if prev[E]==-1:break
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=1
        f[x][nx]-=1
        x=nx
    res+=1
print(res)