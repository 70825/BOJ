t = int(input())
for i in range(t):
    A, n = map(int,input().split())
    ans = []
    while 1:
        if A == 0: break
        x = A % n
        ans.append(x)
        A //= n
    flag = True
    for j in range(len(ans)):
        if ans[j] != ans[-1-j]: flag = False
    if flag: print(1)
    else: print(0)