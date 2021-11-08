input = __import__('sys').stdin.readline
from collections import defaultdict as dfd

n = int(input())
arr = []
time = [0] * 50001
place = dfd(lambda: [0] * 50001)

name_set = set()
for i in range(n):
    name, p, *t = input().strip().split()
    if name in name_set: continue
    name_set.add(name)
    t[0] = int(t[0]); t[1] = int(t[1])
    for j in range(t[0], t[1]):
        place[p][j] += 1

ans = []
for name in place.keys():
    res = []
    val = [float('inf'), float('inf'), -1, name] # 시작 시간, 끝나는 시간, 값, name
    p = place[name]
    for i in range(1, 50001):
        if p[i] != 0:
            if val[2] == p[i]: val[1] = i
            if val[2] != p[i]: res.append(val); val = [i, i, p[i], name]
        else:
            if val[2] != -1: res.append(val); val = [float('inf'), float('inf'), -1, name]
    res.sort(key=lambda x: [-x[2], x[3], x[0], x[1]])
    ans.append(res[0])
ans.sort(key = lambda x: [-x[2], x[3], x[0], x[1]])
answer = ans[0]
print(answer[-1], answer[0], answer[1] + 1)