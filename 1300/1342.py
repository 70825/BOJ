def go(pre, val):
    global ans
    if val == len(s):
        ans += 1
        return
    for x in dfd.keys():
        if x != pre and dfd[x] != 0:
            dfd[x] -= 1
            go(x, val+1)
            dfd[x] += 1

s = [*input()]
dfd = __import__('collections').defaultdict(lambda: 0)
for x in s:
    dfd[x] += 1
ans = 0
go('-', 0)
print(ans)