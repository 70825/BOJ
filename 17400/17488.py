n, m = map(int, input().split())
arr = [0] + [*map(int, input().split())]
success = [[] for _ in range(m + 1)]
ans = [[] for _ in range(n + 1)]
for t in range(2):
    new_success = __import__('copy').deepcopy(success)
    for i in range(n):
        L = [*map(int, input().split())]
        for j in range(len(L)-1):
            new_success[L[j]].append(i+1)
    for i in range(1, m+1):
        if len(new_success[i]) <= arr[i]:
            success[i] = new_success[i]
        else: arr[i] = 0

for i in range(m+1):
    for x in success[i]:
        ans[x].append(i)
for i in range(1, n+1):
    if len(ans[i]): print(*ans[i])
    else: print('망했어요')