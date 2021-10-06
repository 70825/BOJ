input = __import__('sys').stdin.readline
from heapq import *

n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])

q = []; heappush(q, arr[0][1])
ans = 1
val = 1
for i in range(1, n):
    while len(q) and q[0] <= arr[i][0]:
        heappop(q)
    heappush(q, arr[i][1])
    ans = max(ans, len(q))
print(ans)