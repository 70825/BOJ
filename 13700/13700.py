from collections import deque
N,S,D,F,B,K=map(int,input().split());k=[]
if K>0:k=[*map(int,input().split())]
Max=10**5;Di=[Max]*(N+1);Di[S]=0
for i in range(len(k)):Di[k[i]]=-1
dx=[F,-B];q=deque([S])
while q:
    x=q.popleft()
    for i in range(2):
        nx=x+dx[i]
        if 0<nx<=N and Di[nx]!=-1 and Di[nx]==Max:
            q.append(nx);Di[nx]=Di[x]+1
print([Di[D],'BUG FOUND'][Di[D]==Max])