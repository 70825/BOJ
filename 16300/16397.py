from collections import deque
M=10**5
N,T,G=map(int,input().split())
D,D[N]=[-1]*M,0
q=deque([N])
while q:
    x=q.popleft()
    if D[x]<T:
        if 2*x<M:
            nx=2*x-10**(len(str(2*x))-1)
            if 0<=nx and D[nx]==-1:q.append(nx);D[nx]=D[x]+1
        if x+1<M and D[x+1]==-1:q.append(x+1);D[x+1]=D[x]+1
print(['ANG',D[G]][D[G]!=-1])