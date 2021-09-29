n = int(input())
arr = [*map(int, input().split())]
ans = []
for i in range(1, min(arr)+1):
    flag = True
    for x in arr:
        if x % i:
            flag = False
    if flag: ans += [i]
print('\n'.join(map(str,ans)))