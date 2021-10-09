input = __import__('sys').stdin.readline

s, c = map(int, input().split())
arr = [int(input()) for i in  range(s)]
total = sum(arr)
l, r = 0, 10**9
ans = float('inf')
while l <= r:
    mid = (l + r) // 2
    if mid == 0: l = mid + 1; ans = min(ans, total); continue
    count = sum(arr[i] // mid for i in  range(s))
    if count >= c: l = mid + 1; ans = min(ans, total - mid * c)
    else: r = mid - 1
print(ans)