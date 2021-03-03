from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
S=[[float('inf')]*2 for _ in range(n+1)]
D=[[] for _ in range(n+1)]
cycle=False
for i in range(m):
    u,v,w=map(int,input().split())
    D[u].append((v,-w))
S[1][0]=0;q=deque()
V=[0]*(n+1)
for i in range(n):
    for x in range(1,n+1):
        for nx,nt in D[x]:
            if S[nx][0]>S[x][0]+nt:
                S[nx][0]=S[x][0]+nt;S[nx][1]=x
                if i==n-1:V[x]=1;q.append(x)
while q:
    x=q.popleft()
    for nx,nt in D[x]:
        if V[nx]==0:V[nx]=1;q.append(nx)
if S[n][0]==float('inf') or V[n]==1:print(-1)
else:
    Z=[n]
    b=n
    while 1:
        Z.append(S[b][1])
        b=S[b][1]
        if b==1:break
    print(' '.join(map(str,Z[::-1])))