from heapq import *
input = __import__('sys').stdin.readline
n, k = map(int, input().split())
arr = sorted([[*map(int, input().split())] for _ in range(n)], reverse=True)
bag = sorted([int(input()) for _ in range(k)], reverse=True)
use_bag = 0
idx = 0
ans = []
for i in range(n):
    while idx < k and bag[idx] >= arr[i][0]:
        use_bag += 1
        idx += 1
    heappush(ans, arr[i][1])
    if len(ans) > use_bag:
        heappop(ans)
print(sum(ans))