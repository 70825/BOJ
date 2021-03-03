def primeList(n):
    s = [True] * (n+1)

    for i in range(2, int((n) ** 0.5) + 1):
        if s[i]:
            for j in range(i+i, n+1, i):
                s[j] = False

    return [i for i in range(2,n+1) if s[i]]

a, b = map(int, input().split())
l = primeList(b)

for i in l:
    if i >= a:
        print(i)