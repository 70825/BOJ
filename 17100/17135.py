def NOM():
    for i in range(n):
        for j in range(m):
            if Map[i][j]==1:q.append((i,j))
def Attack(q):
    global k
    target,Dist=[(0,Max),(0,Max),(0,Max)],[Max,Max,Max]
    while q:
        x,y=q.popleft()
        for i in range(3):
            z=abs(n-x)+abs(S[i]-y)
            if Dist[i]>z:Dist[i]=z;target[i]=(x,y)
            elif Dist[i]==z and y<target[i][1]:target[i]=(x,y)
    for t,(x,y) in enumerate(target):
        if Map[x][y]==1 and Dist[t]<=d:Map[x][y]=0;k+=1
import itertools
import copy
from collections import deque
Max=float('inf')
n,m,d=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
Castle=[i for i in range(m)]
Archer=itertools.combinations(Castle,3)
ans=0
q=deque()
for S in Archer:
    Map,k=copy.deepcopy(D),0
    while 1:
        NOM()
        if len(q)==0:break
        Attack(q)
        Map=[[0]*m]+Map[:n-1]
    ans=max(ans,k)
print(ans)