from collections import deque
N=int(input())
check=[0]*(N+1);check[1]=1
q=deque();q.append(1)
S=[[] for _ in range(N+1)]
for i in range(int(input())):
    a,b=map(int,input().split())
    S[a].append(b)
    S[b].append(a)
while q:
    x=q.popleft()
    for i in range(len(S[x])):
        if check[S[x][i]]==0:
            q.append(S[x][i])
            check[S[x][i]]=1
print(sum(check)-1)