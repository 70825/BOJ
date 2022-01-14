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
MAX_VAL = 200000

while 1:
    a = [*map(int, input().split())]
    if a[0] == 0: break
    n, q = a
    arr = [0] + [i + 100001 for i in map(int, input().split())]

    query = [[*map(int, input().split())] + [i] for i in range(q)]
    query.sort(key=lambda x: [x[0]//sqrt(n), x[1]])
    
    dcnt = 0
    cnt = [0] * (MAX_VAL + 1)
    count = [0] * (MAX_VAL + 1)
    result = [0] * q

    s, e= query[0][0], query[0][1]
    for i in range(s, e+1): add(i)
    result[query[0][2]] = dcnt

    for i in range(1, q):
        qs, qe, idx = query[i]
        while qs < s:
            s -= 1; add(s)
        while qs > s:
            sub(s); s += 1
        while e < qe:
            e += 1; add(e)
        while e > qe:
            sub(e); e -= 1
        result[idx] = dcnt

    for i in range(q):
        print(result[i])