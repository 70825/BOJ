n, m = map(int, input().split())
arr = sorted([*map(int, input().split())])
idx = -1
for i in range(1, n):
    if arr[i] > 0 > arr[i-1]:
        idx = i
        break
ans = 0
if idx == -1:
    if arr[0] > 0: ans = arr[-1] + sum(2 * arr[i] for i in range(n - m - 1, -1, -m))
    else: ans = arr[0] + sum(2 * arr[i] for i in range(m, n, m))
    print(abs(ans))
else:
    if abs(arr[0]) > arr[-1]:
        ans = abs(arr[0]) + sum(2 * abs(arr[i]) for i in range(m, idx, m))
        ans += sum(2 * arr[i] for i in range(n - 1, idx - 1, -m))
    else:
        ans = arr[-1] + sum(2 * arr[i] for i in range(n - m - 1, idx - 1, -m))
        ans += sum(2 * abs(arr[i]) for i in range(0, idx, m))
    print(ans)