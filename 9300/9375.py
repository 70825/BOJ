from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    if n == 0:print(0);continue
    D = defaultdict(lambda: 1)
    for i in range(n):
        a,b = input().split()
        D[b]+=1
    ans = 0
    for k in D.keys():
        if ans == 0:ans = D[k]
        else: ans *= D[k]
    print(ans-1)