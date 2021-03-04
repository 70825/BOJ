from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
s,e=map(int,input().split())
s-=1;e-=1
check=[-1]*n
check[s]=0
D={}
for i in range(m):
    x,y=map(int,input().split())
    x-=1;y-=1
    if x not in D:D[x]=[y]
    else:D[x].append(y)
    if y not in D:D[y]=[x]
    else:D[y].append(x)
q=deque([s])
while q:
    x=q.popleft()
    for nx in [x+1,x-1]:
        if 0<=nx<n and check[nx]==-1:
            check[nx]=check[x]+1;q.append(nx)
    if x in D:
        for nx in D[x]:
            if check[nx]==-1:
                check[nx]=check[x]+1;q.append(nx)
print(check[e])