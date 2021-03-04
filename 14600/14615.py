def bfs(s,graph,check):
    q=deque([s])
    check[s]=1
    while q:
        x=q.popleft()
        for nx in graph[x]:
            if check[nx]==0:
                check[nx]=1
                q.append(nx)

from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[] for _ in range(n)]
C=[[] for _ in range(n)]
S1=[0]*n
S2=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    D[a-1].append(b-1)
    C[b-1].append(a-1)
S1[0]=1
bfs(0,D,S1)
S2[n-1]=1
bfs(n-1,C,S2)
for _ in range(int(input())):
    k=int(input())
    if S1[k-1]==1 and S2[k-1]==1:print('Defend the CTP')
    else:print('Destroyed the CTP')