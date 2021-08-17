n = int(input())
if n == 1:print(0); exit()

arr = [*map(int, input().split())]
val = [[] for _ in range(n)]
up = [0] * n

for x in arr[1:]:
    up[x] += 1

q = __import__('collections').deque()
for i in range(1, len(arr)):
    if up[i] == 0:
        q.append([i, 0])
while q:
    x, t = q.popleft()
    if x == 0: print(t)
    nx = arr[x]
    val[nx].append(t + 1)
    up[nx] -= 1
    if up[nx] == 0:
        val[nx].sort(reverse=True)
        nt = [val[nx][i] + i for i in range(len(val[nx]))]
        q.append([nx, max(nt)])