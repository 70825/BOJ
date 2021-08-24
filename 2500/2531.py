n, d, k, c = map(int, input().split())
val = [int(input()) for i in range(n)]
sushi = [0] * 3001
q = __import__('collections').deque()
num = 0
flag = (c in val) ^ 1
for i in range(k):
    q.append(val[i])
    if not sushi[val[i]]: num += 1
    sushi[val[i]] += 1
ans = num if sushi[c] else num + 1
idx = k % n
while idx != k-1:
    e = q.popleft()
    sushi[e] -= 1
    if not sushi[e]: num -= 1

    q.append(val[idx])
    if not sushi[val[idx]]: num += 1
    sushi[val[idx]] += 1

    ans = max(ans, num) if sushi[c] else max(ans, num + 1)
    idx = (idx + 1) % n
print(ans)