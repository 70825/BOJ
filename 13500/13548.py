def add(x):
    global dcnt
    count[cnt[arr[x]]] -= 1
    cnt[arr[x]] += 1
    count[cnt[arr[x]]] += 1
    dcnt = max(dcnt, cnt[arr[x]])

def sub(x):
    global dcnt
    count[cnt[arr[x]]] -= 1
    if dcnt == cnt[arr[x]] and count[cnt[arr[x]]] == 0: dcnt -= 1
    cnt[arr[x]] -= 1
    count[cnt[arr[x]]] += 1

input = __import__('sys').stdin.readline
from math import sqrt
MAX_VAL = 100000

n = int(input())
arr = [0] + [*map(int, input().split())]

q = int(input())
query = [[*map(int, input().split())] + [i] for i in range(q)]
query.sort(key=lambda x: [x[0]//sqrt(n), x[1]])

dcnt = 0
cnt = [0] * (MAX_VAL + 1) # 각 값마다 구간에 몇 개가 있는지
count = [0] * (MAX_VAL + 1) # 횟수의 개수
result = [0] * q
visit = [0] * (MAX_VAL + 1)

for i in range(n):
    if visit[i] == 0: count[0] += 1
    visit[i] += 1

s, e= query[0][0], query[0][1]
for i in range(s, e+1): add(i)
result[query[0][2]] = dcnt

for i in range(1, q):
    qs, qe, idx = query[i]
    while qs < s: # s를 왼쪽으로 늘려야할 때
        s -= 1; add(s)
    while qs > s: # s를 오른쪽으로 줄여야할 때
        sub(s); s += 1
    while e < qe: # e를 오른쪽으로 늘려야할 때
        e += 1; add(e)
    while e > qe:
        sub(e); e -= 1
    result[idx] = dcnt

for i in range(q):
    print(result[i])