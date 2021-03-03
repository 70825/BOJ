from collections import deque
a,b=map(int,input().split())
D=[-1]*1001
q=deque([a]);D[a]=0
for i in range(int(input())):
    n=int(input())
    if n not in q:q.append(n);D[n]=1
while q:
    x=q.popleft()
    if x==b:print(D[x]);exit()
    for nx in [x+1,x-1]:
        if 1<=nx<=1000 and D[nx]==-1:
            q.append(nx);D[nx]=D[x]+1