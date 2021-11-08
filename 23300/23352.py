input = __import__('sys').stdin.readline
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
q = deque()
ans = [0, 0] #길이, 값
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0: continue
        visit = [[0] * m for _ in range(n)]
        q.append([i, j]); visit[i][j] = 1
        val = [[1, arr[i][j] + arr[i][j]]]
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])
                    if visit[nx][ny] == val[0][0]: val.append([val[0][0], arr[i][j] + arr[nx][ny]])
                    if visit[nx][ny] > val[0][0]: val = [[visit[nx][ny], arr[i][j] + arr[nx][ny]]]
        val.sort(key=lambda x:-x[1])
        if val[0][0] > ans[0]: ans = [val[0][0], val[0][1]]
        if val[0][0] == ans[0]: ans[1] = max(ans[1], val[0][1])
print(ans[1])