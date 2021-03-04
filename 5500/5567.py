from collections import deque
n=int(input())
D=[[] for _ in range(n+1)]
S=[0]*(n+1)
for i in range(int(input())):
    a,b=map(int,input().split())
    D[a].append(b)
    D[b].append(a)
q=deque([(1,0)]);S[1]=1
while q:
    x,y=q.popleft()
    for i in range(len(D[x])):
        if S[D[x][i]]==0 and y<2:
            q.append((D[x][i],y+1))
            S[D[x][i]]=1
print(sum(S)-1)