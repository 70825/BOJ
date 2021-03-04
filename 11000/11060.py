from collections import deque
n=int(input())
D=[*map(int,input().split())]
S=[-1]*n;S[0]=0
q=deque([(0)])
while q:
    x=q.popleft()
    for i in range(D[x]):
        if x+(i+1)>=n:break
        if S[x+(i+1)]==-1:
            S[x+(i+1)]=S[x]+1;q.append(x+(i+1))
print(S[n-1])