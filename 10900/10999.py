def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    mid=(s+e)//2
    tree[now]=init(now*2,s,mid)+init(now*2+1,mid+1,e)
    return tree[now]
def lazy_update(now,s,e):
    if lazy[now]==0:return
    tree[now]+=(e-s+1)*lazy[now]
    if(s!=e):
        lazy[now*2]+=lazy[now]
        lazy[now*2+1]+=lazy[now]
    lazy[now]=0
def update(now,s,e,L,R,val):
    lazy_update(now,s,e)
    if L>e or s>R:return
    if L<=s and e<=R:
        tree[now]+=(e-s+1)*val
        if s!=e:
            lazy[now*2]+=val
            lazy[now*2+1]+=val
        return
    mid=(s+e)//2
    update(now*2,s,mid,L,R,val)
    update(now*2+1,mid+1,e,L,R,val)
    tree[now]=tree[now*2]+tree[now*2+1]
def Sum(now,s,e,L,R):
    lazy_update(now,s,e)
    if L>e or R<s:return 0
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return Sum(now*2,s,mid,L,R)+Sum(now*2+1,mid+1,e,L,R)
input=__import__('sys').stdin.readline
from math import ceil,log2
n,m,k=map(int,input().split())
h=ceil(log2(n))
D=[int(input()) for i in range(n)]
tree=[0]*(1<<(h+1))
lazy=[0]*(1<<(h+1))
init(1,0,n-1)
for i in range(m+k):
    inp=[*map(int,input().split())]
    if inp[0]==1:
        a,b,c,d=inp
        update(1,0,n-1,b-1,c-1,d)
    else:
        a,b,c=inp
        print(Sum(1,0,n-1,b-1,c-1))