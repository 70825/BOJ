from heapq import *
input = __import__('sys').stdin.readline
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])
hq = []
for x, y in arr:
    if hq and hq[0] <= x: heappop(hq)
    heappush(hq, y)
print(len(hq))