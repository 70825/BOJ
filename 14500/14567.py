input=__import__('sys').stdin.readline
from collections import deque
n,k=map(int,input().split())
adj=[[] for _ in range(n)]
indegree=[0]*n
result=[0]*n
q=deque()
for i in range(k):
    a,b=map(int,input().split())
    a-=1;b-=1
    adj[a].append(b)
    indegree[b]+=1
for i in range(n):
    if indegree[i]==0:
        q.append(i)
        result[i]=1
for i in range(n):
    x=q.popleft()
    for nx in adj[x]:
        result[nx]=max(result[nx],result[x]+1)
        indegree[nx]-=1
        if indegree[nx]==0:q.append(nx)
print(*result)