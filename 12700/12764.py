from heapq import *
input = __import__('sys').stdin.readline

n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x:[x[0]])
ans = [0] * n
val = 0
q = []
sit = []
for i in range(n):
    heappush(sit, i+1)

for i in range(n):
    while len(q) and q[0][0] <= arr[i][0]:
        e, e_val = heappop(q)
        heappush(sit, e_val)
    sit_val = heappop(sit)
    val = max(val, sit_val)
    ans[sit_val-1] += 1
    heappush(q, [arr[i][1], sit_val])
print(val)
print(*ans[:val])