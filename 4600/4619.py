while 1:
    b, n = map(int, input().split())
    if b == n == 0: break
    if n == 1: print(b); continue
    ans = [-1, 1e9]
    for i in range(1, 1001):
        if ans[1] > abs(b - i ** n):
            ans = [i, abs(b - i ** n)]
    print(ans[0])