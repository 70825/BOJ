n = int(input())
arr = [int(input()) for i in range(n)]
ans = 0
for i in range(n - 1, 0, -1):
    if arr[i] <= arr[i-1]:
        ans += arr[i-1] - (arr[i] - 1)
        arr[i-1] = arr[i] - 1
print(ans)