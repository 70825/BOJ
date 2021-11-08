input = __import__('sys').stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
garo = [[0] * n for _ in range(n)] # 가로
garo_reverse = [[0] * n for _ in range(n)] # 가로 거꾸로
sero = [[0] * n for _ in range(n)] # 세로
sero_reverse = [[0] * n for _ in range(n)] # 세로 거꾸로
dia = [[0] * n for _ in  range(n)] # 대각선 ↘
dia_reverse = [[0] * n for _ in range(n)] # 대각선 거꾸로 ↖
dia2 = [[0] * n for _ in  range(n)] # 대각선 ↙
dia2_reverse = [[0] * n for _ in  range(n)] # 대각선 ↗

ans = 0
# 가로 길이
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and j == 0: garo[i][j] = 1
        if arr[i][j] == 1 and j > 0: garo[i][j] = garo[i][j-1] + 1
        ans = max(ans, garo[i][j])

# 가로 거꾸로 길이
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if arr[i][j] == 1 and j == n-1: garo_reverse[i][j] = 1
        if arr[i][j] == 1 and j < n-1: garo_reverse[i][j] = garo_reverse[i][j+1] + 1
        ans = max(ans, garo_reverse[i][j])

# 세로 길이
for j in range(n):
    for i in range(n):
        if arr[i][j] == 1 and i == 0: sero[i][j] = 1
        if arr[i][j] == 1 and i > 0: sero[i][j] = sero[i-1][j] + 1
        ans = max(ans, sero[i][j])

# 세로 거꾸로 길이
for j in range(n-1, -1, -1):
    for i in range(n-1, -1, -1):
        if arr[i][j] == 1 and i == n-1: sero_reverse[i][j] = 1
        if arr[i][j] == 1 and i < n-1: sero_reverse[i][j] = sero_reverse[i+1][j] + 1
        ans = max(ans, sero_reverse[i][j])

# 대각선 ↘ ↖ - 가로줄부터 (0, 0), (0, 1), ...
for i in range(n):
    x, y = 0, i
    for j in range(n - i):
        if arr[x][y] == 1 and x == 0: dia[x][y] = 1
        if arr[x][y] == 1 and x > 0: dia[x][y] = dia[x-1][y-1] + 1
        ans = max(ans, dia[x][y])
        x += 1
        y += 1
# 대각선 ↘ ↖ - 세로줄부터 (1, 0), (2, 0), ...
for i in range(1, n):
    x, y = i, 0
    for j in range(n - i):
        if arr[x][y] == 1 and y == 0: dia[x][y] = 1
        if arr[x][y] == 1 and y > 0: dia[x][y] = dia[x-1][y-1] + 1
        ans = max(ans, dia[x][y])
        x += 1
        y += 1

# 대각선 반대 ↘ ↖ -> 가로줄부터 (n-1, n-1), (n-1, n-2)
for i in range(n):
    x, y = n-1, n-1-i
    for j in range(n):
        if arr[x][y] == 1 and x == n-1: dia_reverse[x][y] = 1
        if arr[x][y] == 1 and x < n-1: dia_reverse[x][y] = dia_reverse[x+1][y+1] + 1
        ans = max(ans, dia_reverse[x][y])
        x -= 1
        y -= 1

# 대각선 반대 ↘ ↖ -> 세로줄부터 (n-2, n-1), (n-3, n-1)
for i in range(1, n):
    x, y = n - 1 - i, n - 1
    for j in range(n-i):
        if arr[x][y] == 1 and y == n-1: dia_reverse[x][y] = 1
        if arr[x][y] == 1 and y < n-1: dia_reverse[x][y] = dia_reverse[x+1][y+1]+1
        ans = max(ans, dia_reverse[x][y])
        x -= 1
        y -= 1

# 대각선 두번째 ↙ -> 가로줄부터 (0, n-1), (0, n-2), ...
for i in range(n):
    x, y = 0, n-i-1
    for j in range(n-i):
        if arr[x][y] == 1 and x == 0: dia2[x][y] = 1
        if arr[x][y] == 1 and x > 0: dia2[x][y] = dia2[x-1][y+1] + 1
        ans = max(ans, dia2[x][y])
        x += 1
        y -= 1

# 대각선 두번째 ↙ -> 세로줄부터 (0, n-2), (0, n-3), ...
for i in range(1, n):
    x, y = i, n-1
    for j in range(n-i):
        if arr[x][y] == 1 and y == n-1: dia2[x][y] = 1
        if arr[x][y] == 1 and y < n-1: dia2[x][y] = dia2[x-1][y+1] + 1
        ans = max(ans, dia2[x][y])
        x += 1
        y -= 1

# 대각선 두번째 반대로 ↗ -> 가로줄부터 (n-1, 0), (n-1, 1), ...
for i in range(n):
    x, y = n-1, i
    for j in range(n-i):
        if arr[x][y] == 1 and x == n-1: dia2_reverse[x][y] = 1
        if arr[x][y] == 1 and x < n-1: dia2_reverse[x][y] = dia2_reverse[x+1][y-1] + 1
        ans = max(ans, dia2_reverse[x][y])
        x -= 1
        y += 1

# 대각선 두번째 반대로 ↗ -> 세로줄부터 (n-2, 0), (n-3, 0), ...
for i in range(1, n):
    x, y = n-1-i, 0
    for j in range(n-i):
        if arr[x][y] == 1 and y == 0: dia2_reverse[x][y] = 1
        if arr[x][y] == 1 and y > 0: dia2_reverse[x][y] = dia2_reverse[x+1][y-1] + 1
        ans = max(ans, dia2_reverse[x][y])
        x -= 1
        y += 1

# 백돌을 놓았을 때 최대 점수 업데이트 + 모서리 부분 추가
for x in range(n):
    for y in range(n):
        if arr[x][y] == 2:
            x1, y1 = x, y-1 # 가로
            x2, y2 = x, y+1
            if 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, garo[x1][y1] + 1 + garo_reverse[x2][y2])
            if 0 <= x1 < n and 0 <= y1 < n: ans = max(ans, garo[x1][y1] + 1)
            if 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, 1 + garo_reverse[x2][y2])
            x1, y1 = x-1, y # 세로
            x2, y2 = x+1, y
            if 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, sero[x1][y1] + 1 + sero_reverse[x2][y2])
            if 0 <= x1 < n and 0 <= y1 < n: ans = max(ans, sero[x1][y1] + 1)
            if 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, 1 + sero_reverse[x2][y2])
            x1, y1 = x-1, y-1 # 대각선 ↘ ↖
            x2, y2 = x+1, y+1
            if 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, dia[x1][y1] + 1 + dia_reverse[x2][y2])
            if 0 <= x1 < n and 0 <= y1 < n: ans = max(ans, dia[x1][y1] + 1)
            if 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, 1 + dia_reverse[x2][y2])
            x1, y1 = x-1, y+1
            x2, y2 = x+1, y-1 # 대각선 ↙ ↗
            if 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, dia2[x1][y1] + 1 + dia2_reverse[x2][y2])
            if 0 <= x1 < n and 0 <= y1 < n: ans = max(ans, dia2[x1][y1] + 1)
            if 0 <= x2 < n and 0 <= y2 < n: ans = max(ans, 1 + dia2_reverse[x2][y2])
print(ans)