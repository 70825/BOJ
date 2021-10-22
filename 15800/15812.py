from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for i in range(n)]
ans = float('inf')
town = sum(1 for i in range(n) for j in range(m) if arr[i][j] == '1')
blank = [(i, j) for i in range(n) for j in range(m) if arr[i][j] =='0']

for a in range(len(blank)):
    for b in range(a+1, len(blank)):
        x1, y1 = blank[a]
        x2, y2 = blank[b]
        val = town
        visit = [[-1] * m for _ in range(n)]
        visit[x1][y1] = 0; visit[x2][y2] = 0
        q = deque([[x1, y1], [x2, y2]])
        res = 0
        while q:
            if val == 0: break
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
                    res = max(res, visit[nx][ny])
                    if arr[nx][ny] == '1': val -= 1
        ans = min(ans, res)
print(ans)