from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
S=[[] for _ in range(n+1)];D=[-1]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    S[x].append(y);S[y].append(x)
q=deque([a]);D[a]=0
while q:
    x=q.popleft()
    for i in range(len(S[x])):
        if D[S[x][i]]==-1:q.append(S[x][i]);D[S[x][i]]=D[x]+1
print(D[b])