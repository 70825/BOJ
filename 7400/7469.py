def init(now,s,e):
    if s==e:
        tree[now]+=[D[s]]
        return tree[now]
    mid=(s+e)//2
    tree[now]=init(now*2,s,mid)+init(now*2+1,mid+1,e)
    return tree[now]
def Find(now,s,e,L,R,val):
    if s>R or e<L:return 0
    if L<=s and e<=R: return bisect(tree[now],val)
    mid=(s+e)//2
    return Find(now*2,s,mid,L,R,val)+Find(now*2+1,mid+1,e,L,R,val)

from math import ceil,log2
from bisect import bisect
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
h=int(ceil(log2(n)))
tree=[[] for _ in range(1<<(h+1))]
D=[*map(int,input().split())]
init(1,0,n-1)
for i in range(1<<(h+1)):
    tree[i]=sorted(tree[i])
for i in range(m):
    a,b,c=map(int,input().split())
    s,e=-10**9,10**9
    while s<=e:
        mid=(s+e)//2
        if Find(1,0,n-1,a-1,b-1,mid)<c: s=mid+1
        else:e=mid-1
    print(s)