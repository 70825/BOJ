from heapq import *
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])
ans = []
for i in range(n):
    heappush(ans, arr[i][1])
    if len(ans) > arr[i][0]:
        heappop(ans)
print(sum(ans))