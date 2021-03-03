import sys
sys.setrecursionlimit(1000000)
input=__import__('sys').stdin.readline
def dfs(x, c):
    col[x] = c
    for y in a[x]:
        if col[y] == 0:
            if not dfs(y, 3-c):return False
        elif col[y] == col[x]:return False
    return True
for _ in range(int(input())):
    V,E = map(int,input().split())
    a = [[] for _ in range(V)]
    col= [0] * V
    for _ in range(E):
        u,v = map(int,input().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)
    ans = True
    for i in range(V):
        if col[i] == 0:
            if not dfs(i, 1):ans = False
    print('YES' if ans else 'NO')