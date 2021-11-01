input = __import__('sys').stdin.readline
dx, dy = [-1, 0, 1, -1, 1, -1, 0, 1], [-1, -1, -1, 0, 0, 1, 1, 1]
n = int(input())
arr = [[*input().strip()] for _ in range(n)]
ans = [0, 0, 0]
for y in range(n):
    for x in range(n):
        if arr[y][x] != '.': continue
        val = 0
        for i in range(8):
            ny, nx = y, x
            white = 0
            while 1:
                ny, nx = ny + dy[i], nx + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if arr[ny][nx] == 'W': white += 1
                    elif arr[ny][nx] == 'B': break
                    else: white = 0; break
                else: white=0; break
            val += white
        if ans[2] < val: ans = [x, y, val]
if ans[2] == 0: print('PASS')
else:
    print(ans[0], ans[1])
    print(ans[2])