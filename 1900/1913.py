dx,dy = [1,0,-1,0],[0,1,0,-1]

n = int(input())
k = int(input())
q = [(0,0,0)]
D = [[-1]*n for _ in range(n)]
val = n*n
D[0][0] = val; val-=1
ans = [-1,-1]
while q:
    if not val: break
    x,y,z = q.pop()
    if D[x][y] == k: ans = [x+1,y+1]
    nx, ny = x+dx[z], y+dy[z]
    if 0<=nx<n and 0<=ny<n and D[nx][ny] == -1:
        D[nx][ny] = val
        val -= 1
        q.append((nx,ny,z))
    else:
        z = (z+1)%4
        q.append((x,y,z))
for i in range(n):
    print(*D[i])
print(*ans)