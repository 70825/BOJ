from collections import deque
input=__import__('sys').stdin.readline
n=int(input())
Parent=[-1]*n
Tree=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    Tree[a-1].append(b-1)
    Tree[b-1].append(a-1)
q=deque([0])
while q:
    x=q.popleft()
    for nx in Tree[x]:
        if Parent[nx]==-1:Parent[nx]=x;q.append(nx)
for i in range(1,n):
    print(Parent[i]+1)