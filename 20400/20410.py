m, seed, x1, x2 = map(int,input().split())
for a in range(m):
    for c in range(m):
        if (a*seed+c)%m == x1 and (a*x1+c)%m == x2:
            print(a,c);exit()