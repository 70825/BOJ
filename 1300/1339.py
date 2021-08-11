n = int(input())
dfd = __import__('collections').defaultdict(lambda: 0)
for _ in range(n):
    s = input()
    for i in range(len(s)):
        dfd[s[i]] += (10 ** (len(s) - 1 - i))
ans = sum(x * (9 - i) for i, x in enumerate(sorted(dfd.values(), reverse=True)))
print(ans)