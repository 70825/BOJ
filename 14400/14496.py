from collections import deque
a,b=map(int,input().split())
n,m=map(int,input().split())
S=[-1]*(n+1)
D=[[] for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    D[x].append(y);D[y].append(x)
q,S[a]=deque([a]),0
while q:
    x=q.popleft()
    for i in range(len(D[x])):
        if S[D[x][i]]==-1:q.append(D[x][i]);S[D[x][i]]=S[x]+1
print(S[b])