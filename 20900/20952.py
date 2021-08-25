input = __import__('sys').stdin.readline
MOD = 10**9 + 7
n, m = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
val = [i for i in range(7)]
zero = [False] * 7
count = [0] * 7
for i in range(n): count[A[i] % 7] += 1
plus = 0
for i in range(m):
    new_val = val.copy()
    new_count = count.copy()
    new_zero = zero.copy()
    for j in range(7):
        if zero[j]: continue
        new_val[j] = (val[j] + B[i]) % 7
        if new_val[j] == 0:
            new_count[j] = 0
            new_zero[j] = True
    if sum(new_count) != 0:
        plus = (plus + B[i]) % MOD
        val, count, zero = new_val, new_count, new_zero
ans = [(A[i] + plus) % MOD for i in range(n) if not zero[A[i] % 7]]
print(len(ans))
print(*ans)