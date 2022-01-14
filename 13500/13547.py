input = __import__('sys').stdin.readline
from math import sqrt
MAX_VAL = 1000000

n = int(input())
arr = [0] + [*map(int, input().split())]
sqrtN = int(sqrt(n) + 1)
query = []

m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    query.append([l, r, i])
query.sort(key = lambda x: [x[0] // sqrtN, x[1]])

dcnt = 0 # 서로 다른 수의 개수
cnt = [0] * (MAX_VAL + 1) # 수가 몇 개 있는지
result = [0] * m # 쿼리당 답
s, e = query[0][0], query[0][1]
for i in range(s, e + 1):
    cnt[arr[i]] += 1
    if cnt[arr[i]] == 1: dcnt += 1
result[query[0][2]] = dcnt

for i in range(1, m):
    while query[i][0] < s: # s의 값을 왼쪽으로 늘려야할때
        s -= 1
        cnt[arr[s]] += 1
        if cnt[arr[s]] == 1: dcnt += 1
    while e < query[i][1]: # e의 값을 오른쪽으로 늘려야할때
        e += 1
        cnt[arr[e]] += 1
        if cnt[arr[e]] == 1: dcnt += 1
    while query[i][0] > s: # s의 값을 오른쪽으로 줄여야할때
        cnt[arr[s]] -= 1
        if cnt[arr[s]] == 0: dcnt -= 1
        s += 1
    while e > query[i][1]: # e의 값을 왼쪽으로 줄여야할때
        cnt[arr[e]] -= 1
        if cnt[arr[e]] == 0: dcnt -= 1
        e -= 1
    result[query[i][2]] = dcnt

for i in range(m):
    print(result[i])