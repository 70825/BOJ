from heapq import *
arr = []
for i in range(int(input())):
    heappush(arr, int(input()))
ans = 0
while len(arr) != 1:
    x = heappop(arr)
    y = heappop(arr)
    ans += x + y
    heappush(arr, x + y)
print(ans)