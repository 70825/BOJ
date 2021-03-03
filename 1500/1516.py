input=__import__('sys').stdin.readline
from collections import deque
n=int(input())
indegree=[0]*n
adj=[[] for _ in range(n)]
q=deque()
time=[0]*n
result=[0]*n
for i in range(n):
    t,*D=map(int,input().split())
    time[i]=t
    for j in range(len(D)-1):
        indegree[i]+=1
        adj[D[j]-1].append(i)
    if indegree[i]==0:
        result[i] = t
        q.append(i)
for i in range(n):
    curr=q.popleft()
    for nx in adj[curr]:
        result[nx]=max(result[nx],result[curr]+time[nx])
        indegree[nx]-=1
        if indegree[nx]==0:q.append(nx)
print('\n'.join(map(str,result)))