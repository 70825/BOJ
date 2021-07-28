t = 1
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0: break

    ans = v // p * l + (l if v % p >= l else v % p)
    print(f'Case {t}: {ans}')
    t += 1