def update(now, s, e):
    if s == e:
        tree[now] = s
        return tree[now]
    mid = (s + e) // 2
    tree[now] = tree[now*2] if arr[update(now * 2, s, mid)] <= arr[update(now * 2 + 1, mid+1, e)] else tree[now*2+1]
    return tree[now]

def find_min(now, s, e, L, R):
    if s > R or e < L: return -1
    if L <= s and e <= R: return tree[now]
    mid = (s + e) // 2
    x = find_min(now * 2, s, mid, L, R)
    y = find_min(now * 2 + 1, mid + 1, e, L, R)
    if x == -1: return y
    if y == -1: return x
    return x if arr[x] <= arr[y] else y

def go(l, r):
    global res
    idx = find_min(1, 0, n-1, l, r)
    res = max(res, (r - l + 1) * arr[idx])
    if l < idx: go(l, idx-1)
    if r > idx: go(idx+1, r)

import sys
sys.setrecursionlimit(200000)
input = __import__('sys').stdin.readline
while 1:
    arr = [*map(int, input().split())]
    if arr[0] == 0: break

    n = arr[0]
    arr = arr[1:]
    tree = [0] * (4 * n)
    update(1, 0, n-1)

    res = 0
    go(0, n-1)
    print(res)