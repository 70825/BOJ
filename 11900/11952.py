from heapq import *
from collections import deque
input=__import__('sys').stdin.readline
n,m,k,s=map(int,input().split())
P,Q=map(int,input().split())
path=[-1]*n
cost=[P]*n
D=[[] for _ in range(n)]
q=deque()
for i in range(k):
    k=int(input())-1
    q.append(k);path[k]=0;cost[k]=float('inf')
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    D[a].append(b);D[b].append(a)
while q:
    x=q.popleft()
    for nx in D[x]:
        nt=path[x]+1
        if path[nx]==-1 and nt<=s:
            path[nx]=nt;cost[nx]=Q;q.append(nx)
q=[];heappush(q,[0,0])
money=[float('inf')]*n;money[0]=0
while q:
    x,t=heappop(q)
    if money[x]!=t:continue
    for nx in D[x]:
        nt = money[x]+cost[nx]
        if money[nx]>nt:
            money[nx]=nt;heappush(q,[nx,nt])
print(money[n-1]-cost[n-1])