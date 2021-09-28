from heapq import *
input = __import__('sys').stdin.readline

n, l = map(int, input().split())
arr = [*map(int, input().split())]
pq = []
ans = []
for i in range(n):
    j = i - l + 1
    heappush(pq, (arr[i], i))
    while pq and pq[0][1] < j:
        heappop(pq)
    ans.append(pq[0][0])
print(*ans)