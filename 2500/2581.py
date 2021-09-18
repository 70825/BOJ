N = 10001
prime = [True] * 10001
prime[1] = False
for i in range(2, N):
    if not prime[i]: continue
    for j in range(i+i, N, i):
        prime[j] = False

m = int(input())
n = int(input())

ans = 0
min_val = float('inf')
for i in range(m, n + 1):
    if prime[i]:
        ans += i
        min_val = min(min_val, i)
print([-1, f'{ans}\n{min_val}'][ans != 0])