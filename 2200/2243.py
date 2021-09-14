def update(now, s, e, idx, val):
    if idx < s or idx > e: return tree[now]
    if s == e:
        tree[now] += val
        return tree[now]
    mid = (s + e)//2
    tree[now] = update(now*2, s, mid, idx, val) + update(now*2+1, mid+1, e, idx, val)
    return tree[now]

def sum_(now, s, e, k):
    global res
    if s == e and not res:
        return s
    
    mid = (s + e)//2
    if res == 0 and now * 2 <= size and tree[now*2] >= k:
        res = sum_(now*2, s, mid, k)
        return res
    
    k -= tree[now*2]
    if res == 0 and now * 2 + 1 <= size and tree[now * 2 + 1] >= k:
        res = sum_(now*2+1, mid+1, e, k)
        return res

from math import ceil, log2
input = __import__('sys').stdin.readline
N = int(1e6) + 1
h = ceil(log2(N))
size = 1 << (h + 1)
res = 0

n = int(input())
tree = [0] * (2 * size)
for i in range(n):
    a, *etc = map(int, input().split())
    res = 0
    if a == 1:
        b = etc[0]
        idx = sum_(1, 0, N, b)
        print(idx)
        update(1, 0, N, idx, -1)
    else:
        b, c = etc
        update(1, 0, N, b, c)