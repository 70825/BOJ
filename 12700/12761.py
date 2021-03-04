def go(x,nx):
    if 0<=nx<=100000 and D[nx]==-1:
        D[nx]=D[x]+1;q.append(nx)
from collections import deque
a,b,n,m=map(int,input().split())
D=[-1]*(100001)
D[n]=0;q=deque([n])
while q:
    x=q.popleft()
    for nx in [x+1,x-1,x-a,x-b,x+a,x+b,a*x,b*x]:
        go(x,nx)
print(D[m])