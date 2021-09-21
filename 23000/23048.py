n = int(input())
arr = [1] * (n + 1)
visit = [False] * (n + 1)
color = 1
for i in range(2, n+1):
    if not visit[i]:
        color += 1
        arr[i] = color
        visit[i] = True
        for j in range(i+i, n+1, i):
            visit[j] = True
            arr[j] = color
print(color)
print(*arr[1:])