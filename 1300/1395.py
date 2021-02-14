def lazy_update(now,s,e):
    if lazy[now]==0:return
    tree[now]=(e-s+1)-tree[now]
    if s!=e:
        lazy[now*2]^=1
        lazy[now*2+1]^=1
    lazy[now]=0
def update(now,s,e,L,R):
    lazy_update(now,s,e)
    if s>R or e<L:return tree[now]
    if L<=s and e<=R:
        tree[now]=(e-s+1)-tree[now]
        if s!=e:
            lazy[now*2]^=1
            lazy[now*2+1]^=1
        return tree[now]
    mid=(s+e)//2
    tree[now]=update(now*2,s,mid,L,R)+update(now*2+1,mid+1,e,L,R)
    return tree[now]
def Sum(now,s,e,L,R):
    lazy_update(now,s,e)
    if s>R or e<L:return 0
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return Sum(now*2,s,mid,L,R)+Sum(now*2+1,mid+1,e,L,R)
from math import ceil,log2
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
h=int(ceil(log2(n)))
tree=[0]*(1<<(h+1))
lazy=[0]*(1<<(h+1))
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:update(1,0,n-1,b-1,c-1)
    else:print(Sum(1,0,n-1,b-1,c-1))