n, k = map(int, input().split())
MOD = int(1e9+7)
expo = MOD - 2

A, B = 1, 1
for i in range(1, n+1):
    A = (i * A) % MOD
for i in range(1, k+1):
    B = (i * B) % MOD
for i in range(1, n-k+1):
    B = (i * B) % MOD

B2 = 1 # B^(MOD-2)
while expo:
    if expo % 2: B2 = (B * B2) % MOD
    B = (B * B) % MOD
    expo //= 2

res = (A * B2) % MOD
print(res)