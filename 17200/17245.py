input = __import__('sys').stdin.readline
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
computer = sum(sum(arr[i]) for i in range(n))
l, r = 0, 10**7
ans = float('inf')
while l <= r:
    mid = (l + r) // 2
    res = sum(min(arr[i][j], mid) for i in range(n) for j in range(n))
    if res * 2 >= computer: ans = min(ans, mid); r = mid - 1
    else: l = mid + 1
print(ans)