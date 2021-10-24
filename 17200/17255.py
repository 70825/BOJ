def go(arr, l, r):
    if l == 0 and r == len(n) - 1:
        res.add(','.join(arr))
        return
    if l != 0: go(arr+[n[l-1] + arr[-1]], l-1, r)
    if r != len(n) - 1: go(arr+[arr[-1]+n[r+1]], l, r+1)

n = input()
res = set()
for i in range(len(n)):
    go([n[i]], i, i)
print(len(res))