from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[] for _ in range(n)]
S=[-1]*n
for i in range(m):
    a,b=map(int,input().split())
    D[a-1].append(b-1)
S[0]=0
q=deque([0])
while q:
    x=q.popleft()
    for nx in D[x]:
        if S[nx]==-1 or S[nx]>S[x]+1:
            S[nx]=S[x]+1;q.append(nx)
print(S[n-1])