from heapq import *
n=int(input())
S=[[float('inf')]*2 for _ in range(n+1)]
D=[[] for _ in range(n+1)]
for i in range(int(input())):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
s,e=map(int,input().split())
S[s][0]=0;q=[];heappush(q,(0,s))
while q:
    t,x=heappop(q)
    if S[x][0]!=t:continue
    for nx,nt in D[x]:
        if S[nx][0]>t+nt:
            S[nx][0]=t+nt;S[nx][1]=x
            heappush(q,(t+nt,nx))
K,ans=[e],S[e][1]
while 1:
    if ans==float('inf'):break
    K.append(ans)
    ans=S[ans][1]
print(S[e][0])
print(len(K))
print(*K[::-1])