n, l = map(int, input().split())
arr = sorted([*map(int, input().split())])

ans = 1
val = arr[0] - 0.5 + l
for i in range(1, n):
    if val >= arr[i] + 0.5: continue
    ans += 1
    val = arr[i] - 0.5 + l

print(ans)