input=__import__('sys').stdin.readline
from collections import deque
for __ in range(int(input())):
    n,m,p=map(int,input().split())
    adj=[[] for _ in range(m)]
    indegree=[0]*m
    for i in range(p):
        a,b=map(int,input().split())
        a-=1;b-=1
        adj[a].append(b)
        indegree[b]+=1
    q=deque()
    D=[{} for i in range(m)]
    result=[0]*m
    for i in range(m):
        if indegree[i]==0:
            q.append(i)
            D[i][1]=1
            result[i]=1
    for i in range(m):
        x=q.popleft()
        for nx in adj[x]:
            indegree[nx]-=1
            if result[x] in D[nx]:D[nx][result[x]]+=1
            else:D[nx][result[x]]=1
            k=max(D[nx].keys())
            if D[nx][k]>1:result[nx]=k+1
            else:result[nx]=k
            if indegree[nx]==0: q.append(nx)
    print(n,max(result))