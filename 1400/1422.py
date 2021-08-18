from functools import cmp_to_key
k, n = map(int, input().split())
arr = sorted([input() for _ in range(k)], key=cmp_to_key(lambda a, b: 1 if int(a+b) < int(b+a) else -1))
long = sorted(arr, key=cmp_to_key(lambda a, b: 1 if len(a) < len(b) else 0 if len(a) == len(b) and int(a+b) < int(b+a) else -1))[0]
ans = []
flag = False
for i in range(k):
    ans.append(arr[i])
    if arr[i] == long and not flag:
        ans.append(arr[i] * (n - k))
        flag = True
print(''.join(ans))