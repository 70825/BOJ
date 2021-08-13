n = int(input())
if n == 0:
    print(0)
    exit()
arr = sorted([[*map(int, input().split())] for _ in range(n)], reverse=True)
max_day = max(arr[i][1] for i in range(n)) + 1
ans = 0
visit = [0] * max_day
for val, day in arr:
    for i in range(day, 0, -1):
        if not visit[i]:
            visit[i] = 1
            ans += val
            break
print(ans)