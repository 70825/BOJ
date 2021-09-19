def go(last_x, last_y, length, fill):
    if fill:
        for x in range(last_x - length, last_x):
            for y in range(last_y - length, last_y):
                arr[x][y] = ' '
        return
    next_len = length//3
    if length >= 3:
        for i in range(3):
            for j in range(3):
                nx = last_x - next_len * i
                ny = last_y - next_len * j
                go(nx, ny, next_len, 1 if i == j == 1 else 0)

n = int(input())
arr = [['*'] * n for _ in range(n)]
go(n, n, n, 0)
for i in range(n):
    print(''.join(arr[i]))