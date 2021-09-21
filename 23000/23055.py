def go(x1, y1, x2, y2):
    arr[x1][y1] = '*'
    arr[x2][y2] = '*'
    x1 += 1; y1 += 1
    x2 += 1; y2 -= 1
    if x1 != n-1: go(x1, y1, x2, y2)

n = int(input())
if n <= 4:
    arr = [['*'] * n for _ in range(n)]
    for i in range(n):
        print(''.join(arr[i]))
    exit()
arr = [[' '] * n for _ in range(n)]
for i in range(n):
    arr[i][0] = '*'
    arr[i][-1] = '*'
    arr[0][i] = '*'
    arr[-1][i] = '*'
go(1, 1, 1, n-2)
go(n-2, 1, n-2, n-2)
for i in range(n):
    print(''.join(arr[i]))