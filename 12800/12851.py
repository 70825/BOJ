from collections import deque
Max=100001
N,K=map(int,input().split())
S=[[Max,0] for _ in range(Max)]
q=deque([N]);S[N][0],S[N][1]=0,1
while q:
    x=q.popleft()
    for nx in [x+1,x-1,2*x]:
        if 0<=nx<Max:
            if S[nx][0]==Max:q.append(nx);S[nx][0],S[nx][1]=S[x][0]+1,S[x][1]
            elif S[nx][0]==S[x][0]+1:S[nx][1]+=S[x][1]
print(S[K][0])
print(S[K][1])