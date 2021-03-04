def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    mid=(s+e)//2
    tree[now]=init(now*2,s,mid)^init(now*2+1,mid+1,e)
    return tree[now]
def lazy_update(now,s,e):
    if lazy[now]==0:return
    tree[now]^=lazy[now]*((e-s+1)%2)
    if s!=e:
        lazy[now*2]^=lazy[now]
        lazy[now*2+1]^=lazy[now]
    lazy[now]=0
def update(now,s,e,L,R,val):
    lazy_update(now,s,e)
    if s>R or e<L:return tree[now]
    if L<=s and e<=R:
        tree[now]^=val*((e-s+1)%2)
        if s!=e:
            lazy[now*2]^=val
            lazy[now*2+1]^=val
        return tree[now]
    mid=(s+e)//2
    tree[now]=update(now*2,s,mid,L,R,val)^update(now*2+1,mid+1,e,L,R,val)
    return tree[now]
def Xor(now,s,e,L,R):
    lazy_update(now,s,e)
    if s>R or e<L:return 0
    if L<=s and e<=R: return tree[now]
    mid=(s+e)//2
    return Xor(now*2,s,mid,L,R)^Xor(now*2+1,mid+1,e,L,R)

from math import ceil,log2
input=__import__('sys').stdin.readline
n=int(input())
h=int(ceil(log2(n)))
D=[*map(int,input().split())]
tree=[0]*(1<<(h+1))
lazy=[0]*(1<<(h+1))
init(1,0,n-1)
for i in range(int(input())):
    inp=[*map(int,input().split())]
    if inp[0]==1:
        t,a,b,c=inp
        update(1,0,n-1,min(a,b),max(a,b),c)
    else:
        t,a,b=inp
        print(Xor(1,0,n-1,min(a,b),max(a,b)))