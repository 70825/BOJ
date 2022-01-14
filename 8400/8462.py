input = __import__('sys').stdin.readline
from math import sqrt
MAX = 100000

n, t = map(int, input().split())
arr = [0] + [*map(int, input().split())]
sqrtN = int(sqrt(n))

query = []
for i in range(t):
    l, r = map(int, input().split())
    query.append([l, r, i])
query.sort(key = lambda x: [x[0] // sqrtN, x[1]])

dcnt = 0
cnt = [0] * (MAX * 10 + 1)
result = [0] * (MAX + 1)

s, e = query[0][0], query[0][1]
for i in range(s, e + 1):
    old_ks = cnt[arr[i]]
    dcnt -= old_ks * old_ks * arr[i]
    cnt[arr[i]] += 1
    new_ks = cnt[arr[i]]
    dcnt += new_ks * new_ks * arr[i]
result[query[0][2]] = dcnt

for i in range(1, t):
    while query[i][0] != s:
        if query[i][0] < s:
            s -= 1
            dcnt -= cnt[arr[s]] * cnt[arr[s]] * arr[s]
            cnt[arr[s]] += 1
            dcnt += cnt[arr[s]] * cnt[arr[s]] * arr[s]
        else:
            dcnt -= cnt[arr[s]] * cnt[arr[s]] * arr[s]
            cnt[arr[s]] -= 1
            dcnt += cnt[arr[s]] * cnt[arr[s]] * arr[s]
            s += 1
    while query[i][1] != e:
        if e < query[i][1]:
            e += 1
            dcnt -= cnt[arr[e]] * cnt[arr[e]] * arr[e]
            cnt[arr[e]] += 1
            dcnt += cnt[arr[e]] * cnt[arr[e]] * arr[e]
        else:
            dcnt -= cnt[arr[e]] * cnt[arr[e]] * arr[e]
            cnt[arr[e]] -= 1
            dcnt += cnt[arr[e]] * cnt[arr[e]] * arr[e]
            e -= 1
    result[query[i][2]] = dcnt

for i in range(t):
    print(result[i])