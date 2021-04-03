from math import log2
input = __import__('sys').stdin.readline
max_p = 30
n,k,m= map(int,input().split())
st = [*map(int,input().split())]
yt = [*map(int,input().split())]
pt = [[-1]*max_p for _ in range(k)]
ans = []
for i in range(k):
    pt[i][0] = yt[i]-1
for j in range(max_p-1):
    for i in range(k):
        pt[i][j+1] = pt[pt[i][j]][j]
for i in range(n):
    x = st[i]-1
    diff = m-1
    for j in range(max_p-1,-1,-1):
        if diff >= 2**j:
            diff -= 2**j
            x = pt[x][j]
    ans.append(x+1)
print(*ans)