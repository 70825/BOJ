from heapq import *

n, m = map(int, input().split())
arr = [*map(int, input().split())]
q = []
for i in range(n):
    heappush(q, arr[i])
for i in range(m):
    x = heappop(q)
    y = heappop(q)
    heappush(q, x+y)
    heappush(q, x+y)
print(sum(q))