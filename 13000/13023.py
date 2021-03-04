def go(x,S):
    if len(S)==5: print(1);exit()
    for nx in D[x]:
        if nx not in S:
            go(nx,S+[nx])
n,m = map(int,input().split())
D = [[] for _ in range(n)]
for i in range(m):
    x,y= map(int,input().split())
    D[x].append(y)
    D[y].append(x)
for i in range(n):
    go(i,[i])
print(0)