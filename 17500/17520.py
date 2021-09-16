n = int(input())
MOD = 16769023
res = 2
while n > 2:
    res = (res * 2) % MOD
    n -= 2
print(res)