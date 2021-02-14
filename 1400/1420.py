def edge(x,y,z=1):
    c[(x,y)]=z
    path[x].append(y)
    path[y].append(x)
from collections import deque,defaultdict
input=__import__('sys').stdin.readline
INF=10**10
n,m=map(int,input().split())
D=[input() for _ in range(n)]
nm=2*(n*m+1)
S,E=-1,-1
c=defaultdict(int)
f=defaultdict(int)
path=[[] for _ in range(nm)]
ans=0
for i in range(n):
    for j in range(m):
        if D[i][j]=='K':S=ans+1;sx,sy=i,j
        if D[i][j]=='H':E=ans;ex,ey=i,j
        edge(ans,ans+1)
        ans+=2
if (n==1 and m==1) or S==-1 or E==-1 or (abs(sx-ex)+abs(sy-ey)==1):print(-1);exit(0)
for i in range(n*m):edge(i*2,i*2+1)
t=0
for i in range(n):
    for j in range(m):
        if i+1<n and D[i][j]!='#' and D[i+1][j]!='#':
            nt=t+2*m
            edge(t+1,nt,INF)
            edge(nt+1,t,INF)
        if j+1<m and D[i][j]!='#' and D[i][j+1]!='#':
            nt=t+2
            edge(t+1,nt,INF)
            edge(nt+1,t,INF)
        t+=2
res=0
while 1:
    q=deque([S])
    prev=[-1]*nm
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[(x,nx)]-f[(x,nx)]>0 and prev[nx]==-1:
                prev[nx]=x;q.append(nx)
    if prev[E]==-1:break
    x=E
    while x!=S:
        nx=prev[x]
        f[(nx,x)]+=1
        f[(x,nx)]-=1
        x=nx
    res+=1
print(res)