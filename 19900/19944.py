n, m = map(int,input().split())
if m <= n and m != 1 and m != 2:
    print('OLDBIE!')
elif m <= n:
    print('NEWBIE!')
else:
    print('TLE!')