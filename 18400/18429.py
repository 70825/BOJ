from itertools import permutations as pm

n, k = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
for t in pm(arr,n):
    res = 500
    flag = True
    for x in t:
        res += x - k
        if res < 500: flag = False
    if flag: ans += 1
print(ans)