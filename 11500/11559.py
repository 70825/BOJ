def down():
    for i in range(12):
        for j in range(11):
            for k in range(6):
                if D[j][k] != '.' and D[j+1][k] =='.':
                    D[j+1][k] = D[j][k]
                    D[j][k] = '.'
def puyo(a,b):
    q = deque([[a,b]])
    puyo_q = deque([[a,b]])
    visit[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and D[nx][ny] == D[a][b] and not visit[nx][ny]:
                q.append([nx,ny])
                visit[nx][ny] = 1
                puyo_q.append([nx,ny])
    if len(puyo_q) >= 4:
        while puyo_q:
            x, y = puyo_q.popleft()
            D[x][y] = '.'
        return True
    return False

from collections import deque
dx,dy = [1,-1,0,0],[0,0,1,-1]

D = [[*input()] for _ in range(12)]
ans = 0
while 1:
    visit = [[0]*6 for _ in range(12)]
    flag = False
    for i in range(12):
        for j in range(6):
            if D[i][j] != '.':
                flag = max(flag,puyo(i,j))
    if not flag: break
    else: ans += 1
    down()
print(ans)