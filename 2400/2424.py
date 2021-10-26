from collections import deque
input = __import__('sys').stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [[*input().strip()] for _ in range(n)]
p_see = [[float('inf')] * m for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'T': tx, ty = i, j

q = deque()
p_visit = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'V':
            p_visit[i][j] = 0
            q.append([i, j])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'I' and p_visit[nx][ny] == -1:
            q.append([nx, ny])
            p_visit[nx][ny] = p_visit[x][y] + 1

for i in range(n):
    stack = []
    val = [0, 0, float('inf')]
    for j in range(m):
        if arr[i][j] != 'I': val[2] = min(val[2], p_visit[i][j]); val[1] = j
        elif arr[i][j] == 'I' and val[2] != float('inf'):
            stack.append(val)
            val = [j+1, j+1, float('inf')]
        else: val = [j+1, j+1, float('inf')]
    if val[2] != float('inf'): stack.append(val)
    for s, e, val in stack:
        for j in range(s, e+1):
            p_see[i][j] = val

for j in range(m):
    stack = []
    val = [0, 0, float('inf')]
    for i in range(n):
        if arr[i][j] != 'I': val[2] = min(val[2], p_visit[i][j]); val[1] = i
        elif arr[i][j] == 'I' and val[2] != float('inf'):
            stack.append(val)
            val = [i+1, i+1, float('inf')]
        else: val = [i+1, i+1, float('inf')]
    if val[2] != float('inf'): stack.append(val)
    for s, e, val in stack:
        for i in range(s, e+1):
            p_see[i][j] = min(p_see[i][j], val)

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'Y': visit[i][j] = 0; q.append([i, j])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'I' and visit[nx][ny] == -1 and visit[x][y] + 1 < p_see[nx][ny]:
            q.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1

print(['NO','YES'][visit[tx][ty] != -1 and visit[tx][ty] < p_see[tx][ty]])