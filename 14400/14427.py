def init(now,s,e):
    if s==e:
        tree[now]=[D[s],s]
        return tree[now]
    mid=(s+e)//2
    a,b=init(now*2,s,mid)
    c,d=init(now*2+1,mid+1,e)
    if a<c:tree[now]=[a,b]
    elif a>c:tree[now]=[c,d]
    else:tree[now]=[a,min(b,d)]
    return tree[now]
def update(now,s,e,idx,val):
    if s>idx or idx>e:return tree[now]
    if s==e:
        tree[now]=[val,idx]
        return tree[now]
    mid=(s+e)//2
    a,b=update(now*2,s,mid,idx,val)
    c,d=update(now*2+1,mid+1,e,idx,val)
    if a<c:tree[now]=[a,b]
    elif c<a:tree[now]=[c,d]
    else:tree[now]=[a,min(b,d)]
    return tree[now]
def Min(now,s,e,L,R):
    if L>e or R<s:return float('inf')
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    a,b=Min(now*2,s,mid,L,R)
    c,d=Min(now*2+1,mid+1,e,L,R)
    if a<c:return [a,b]
    elif c<a:return [c,d]
    else:return [a,min(b,d)]
input=__import__('sys').stdin.readline
from math import ceil,log2
n=int(input())
D=[*map(int,input().split())]
h=int(ceil(log2(n)))
tree=[[0,0] for _ in range(1<<(h+1))]
init(1,0,n-1)
for i in range(int(input())):
    inp=[*map(int,input().split())]
    if inp[0]==2:print(Min(1,0,n-1,0,n-1)[1]+1)
    else:
        a,b,c=inp
        update(1,0,n-1,b-1,c)