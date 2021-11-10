input = __import__('sys').stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0
val = 0
for i in range(n-1, -1, -1):
    if arr[i] > val:
        ans += 1
        val = arr[i]
print(ans)