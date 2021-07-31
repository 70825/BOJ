n, m = map(int, input().split())
if n == 1: print(1)
elif n == 2:print([(m + 1) // 2, 4][m >= 7])
else:
    if m <= 4: print(m)
    elif m <= 5: print(m - 1)
    else: print(m - 2)