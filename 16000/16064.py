input=__import__('sys').stdin.readline
from collections import deque
n,m=map(int,input().split())
indegree=[0]*n
adj=[[] for _ in range(n)]
q=deque()
for i in range(m):
    s,t,c=map(int,input().split())
    s-=1;t-=1
    adj[s].append([t,c])
    indegree[t]+=1
for i in range(n):
    if indegree[i]==0:q.append(i)
res=[0]*n
for i in range(n):
    x=q.popleft()
    for nx,nt in adj[x]:
        indegree[nx]-=1
        res[nx]=max(res[nx],res[x]+nt)
        if indegree[nx]==0:q.append(nx)
print(max(res))