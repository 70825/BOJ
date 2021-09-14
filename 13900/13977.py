input = __import__('sys').stdin.readline
MOD = int(1e9 + 7)
N = 4 * int(1e6) + 1
factorial = [1] * N
for i in range(1, N):
    factorial[i] = (factorial[i-1] * i) % MOD

for _ in range(int(input())):
    n, k = map(int, input().split())

    A = factorial[n]
    B = (factorial[k] * factorial[n - k]) % MOD

    B2 = 1
    expo = MOD - 2
    while expo:
        if expo % 2: B2 = (B * B2) % MOD
        B = (B * B) % MOD
        expo //= 2

    res = (A * B2) % MOD
    print(res)