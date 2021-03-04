from collections import deque
n,k=map(int,input().split())
D=[[-1]*2 for _ in range(500001)]
q=deque([(n,0)]);Eq=deque()
D[n]=[0,0];ans=0
while q:
    for _ in range(len(q)):
        x,t=q.popleft()
        for i in range(2):
            for nx in [x+1,x-1,2*x]:
                if 0<=nx<=500000 and D[nx][i]==-1 and (t+1)%2==i:
                    D[nx][i]=t+1;Eq.append((nx,D[nx][i]))
    for i in range(2):
        if D[k][i]!=-1 and ans>=D[k][i] and (ans-D[k][i])%2==0:print(ans);exit()
    q=Eq;ans+=1;k+=ans
    if k>500000:print(-1);exit()