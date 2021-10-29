dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
v, m, t = map(int, input().split())
arr = [[] for _ in range(4)]
x, y = 0, 0
k = v
for i in range(8):
    arr[i % 4].append(k)
    x += dx[i%4] * k
    y += dy[i%4] * k
    k = (k * m) % 10
if t <= 8:
    x, y = 0, 0
    for i in range(t):
        x += arr[i % 4][i // 4] * dx[i % 4]
        y += arr[i % 4][i // 4] * dy[i % 4]
    print(x, y)
else:
    val = t - 8
    time = [val // 4] * 4
    for i in range(val % 4): time[i] += 1
    for i in range(4):
        x += arr[i][-1] * dx[i] * time[i]
        y += arr[i][-1] * dy[i] * time[i]
    print(x, y)