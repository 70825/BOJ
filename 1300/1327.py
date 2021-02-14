import sys
from collections import deque
n,k=map(int,input().split())
D=[*map(int,input().split())]
Answer = ''.join(map(str,[i for i in range(1,n+1)]))
check={''.join(map(str,D)): 0}
q=deque([''.join(map(str,D))])
while q:
    x=q.popleft()
    if x==Answer:print(check[x]);sys.exit(0)
    D = [*x]
    for i in range(len(D)-k+1):
        nD=D[:i]+D[i:i+k][::-1]+D[i+k:]
        nx = ''.join(map(str,nD))
        if nx not in check:
            check[nx]=check[x]+1
            q.append(nx)
print(-1)