n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
x1 = y1 = x2 = y2 = -1
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            if x1 == y1 == -1: x1, y1 = i, j
            else: x2, y2 = i, j
print(abs(x1-x2)+abs(y1-y2))