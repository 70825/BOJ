from heapq import *
input = __import__('sys').stdin.readline

n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])
q = []
for i in range(n):
    heappush(q, arr[i][1])
    if len(q) > arr[i][0]:
        heappop(q)
print(sum(q))