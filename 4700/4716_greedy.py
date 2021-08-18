while 1:
    n, a, b = map(int, input().split())
    if n == a == b == 0: break
    arr = sorted([[*map(int, input().split())]for _ in range(n)], key=lambda x: -abs(x[1]-x[2]))
    ans = 0
    for k, x, y in arr:
        if x <= y: val = min(k, a)
        else: val = k - min(k, b)
        ans += val * x + (k - val) * y
        a -= val
        b -= k - val
    print(ans)