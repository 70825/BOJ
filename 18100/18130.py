n, q = map(int, input().split())
ans = [-1, float('inf')]
for i in range(n):
    p, k, c = map(int, input().split())
    div = q // k
    if q % k == 0: div -= 1
    val = p + c * div * (div + 1) // 2
    if ans[1] > val:
        ans = [i+1, val]
print(*ans)