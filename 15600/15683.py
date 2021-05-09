def fill(k):
    k = (k + cctv_arr[i]) % 4
    nx, ny = x + dx[k], y + dy[k]
    while 1:
        if nx < 0 or nx >= n or ny < 0 or ny >= m or fill_arr[nx][ny] == 6: break
        fill_arr[nx][ny] = '#'
        nx, ny = nx + dx[k], ny + dy[k]
from collections import deque
from copy import deepcopy
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(n)]
cctv = [(i,j,arr[i][j]) for i in range(n) for j in range(m) if 1 <= arr[i][j] <= 5]
rotate = [[0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [0]]
ans = float('inf')
q = deque([[]])
while q:
    if len(q[0]) == len(cctv): break
    narr = q.popleft()
    num = len(narr)
    for x in rotate[cctv[num][2]-1]:
        q += [narr+[x]]
while q:
    fill_arr = deepcopy(arr)
    cctv_arr = q.popleft()
    for i in range(len(cctv)):
        x, y, num = cctv[i]
        if num not in [0, 6]: fill(0)
        if num in [2, 4, 5]: fill(2)
        if num in [3, 4, 5]: fill(3)
        if num == 5: fill(1)
    val = sum(1 for x in range(n) for y in range(m) if fill_arr[x][y] == 0)
    ans = min(ans, val)
print(ans)