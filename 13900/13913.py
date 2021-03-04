from collections import deque
Max=10**5+1
N,K=map(int,input().split())
D=[[-1]*2 for _ in range(Max)]
q=deque([N]);D[N][0]=0
T=[K];z=K
while q:
    x=q.popleft()
    for nx in [x+1,x-1,2*x]:
        if 0<=nx<Max and D[nx][0]==-1:
            q.append(nx);D[nx][0]=D[x][0]+1;D[nx][1]=x
while D[z][1]!=-1:
    T.append(D[z][1]);z=D[z][1]
print(D[K][0])
print(*reversed(T))