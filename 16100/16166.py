from collections import deque
n=int(input())
K=[[] for _ in range(n+1)]
S=[[] for _ in range(n+1)]
D=[float('inf')]*(n+1)
for i in range(1,n+1):
    a,*b=map(int,input().split())
    for j in range(len(b)):
        K[i].append(b[j])
for i in range(1,n+1):
    for j in range(len(K[i])):
        for x in range(i+1,n+1):
            for y in range(len(K[x])):
                if K[i][j]==K[x][y]:
                    S[i].append(x);S[x].append(i)
q=deque()
for i in range(1,n+1):
    for j in range(len(K[i])):
        if K[i][j]==0:D[i]=0;q.append(i)
while q:
    x=q.popleft()
    for nx in S[x]:
        if D[nx]>D[x]+1:D[nx]=D[x]+1;q.append(nx)
k=int(input())
ans=float('inf')
for i in range(1,n+1):
    for j in range(len(K[i])):
        if K[i][j]==k:ans=min(ans,D[i])
print(-1 if ans==float('inf') else ans)