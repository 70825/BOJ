from collections import deque, Counter
from functools import reduce
import sys
sys.setrecursionlimit(1000000)
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]
def dfs(x, y, cnt):
    group[x][y] = cnt
    for k in range(8):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < h and 0 <= ny <w:
            if a[nx][ny] == 1 and group[nx][ny] == 0:
                dfs(nx, ny, cnt)
while 1:
    w, h = map(int, input().split())
    if w==h==0:break
    a = [[*map(int,input().split())] for _ in range(h)]
    group = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                dfs(i, j, cnt)
    ans = reduce(lambda x, y: x + y, group)
    ans = [x for x in ans if x > 0]
    ans = sorted(list(Counter(ans).values()))
    print(cnt)