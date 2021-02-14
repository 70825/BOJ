from collections import deque
N,M,V=map(int,input().split())
D=[[] for i in range(N)]
check=[0]*N
for i in range(M):
    a,b=map(int,input().split())
    D[a-1].append(b)
    D[b-1].append(a)
for i in range(N):
    D[i].sort()
def dfs(t):
    global check
    check[t-1]=1
    print(t,end=" ")
    for k in D[t-1]:
        if check[k-1]==0:dfs(k)
def bfs(t):
    check=[0]*N
    queue=deque()
    queue.append(t)
    check[t-1]=1
    while queue:
        k=queue.popleft()
        print(k,end=' ')
        for j in D[k-1]:
            if check[j-1]==0:
                check[j-1]=1
                queue.append(j)
dfs(V)
print('')
bfs(V)
print('')