h, n = map(int, input().split())
if h == n:print(1); exit()
a, b = 0, max(h, n) - min(h, n)
arr = [[0] * (b+1) for _ in range(b+1)]
for i in range(b+1):
    for j in range(b+1):
        if i == j == 0 or j > i : continue
        elif i != 0 and j == 0: arr[i][j] = 1
        elif i == j: arr[i][j] = arr[i][j-1]
        else: arr[i][j] = arr[i-1][j] + arr[i][j-1]
print(arr[b][b])