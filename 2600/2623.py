input=__import__('sys').stdin.readline
from collections import deque
n,m=map(int,input().split())
indegree=[0]*n
adj=[[] for _ in range(n)]
for i in range(m):
    K,prev,*curr=map(int,input().split())
    for j in range(K-1):
        indegree[curr[j]-1]+=1
        adj[prev-1].append(curr[j]-1)
        prev = curr[j]
result=[0]*n
q=deque()
for i in range(n):
    if indegree[i] == 0: q.append(i)
for i in range(n):
    if not q:print(0);exit(0)
    curr = q.popleft()
    result[i] = curr+1
    for nx in adj[curr]:
        indegree[nx]-=1
        if indegree[nx]==0:
            q.append(nx)
print('\n'.join(map(str,result)))