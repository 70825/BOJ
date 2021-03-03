input=__import__('sys').stdin.readline
from heapq import *
n,m=map(int,input().split())
indegree=[0]*(n+1)
adj=[[] for _ in range(n+1)]
q=[]
result=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    indegree[b]+=1
for i in range(1,n+1):
    if indegree[i]==0:heappush(q,i)
for i in range(n):
    curr=heappop(q)
    result[i]=curr
    for nx in adj[curr]:
        indegree[nx]-=1
        if indegree[nx]==0:
            heappush(q,nx)
print(*result)