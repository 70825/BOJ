def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    mid=(s+e)//2
    tree[now]=min(init(now*2,s,mid),init(now*2+1,mid+1,e))
    return tree[now]
def update(now,s,e,idx,val):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]=val
        return tree[now]
    mid=(s+e)//2
    tree[now]=min(update(now*2,s,mid,idx,val),update(now*2+1,mid+1,e,idx,val))
    return tree[now]
def Min(now,s,e,L,R):
    if s>R or e<L:return float('inf')
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return min(Min(now*2,s,mid,L,R),Min(now*2+1,mid+1,e,L,R))

from math import ceil,log2
input=__import__('sys').stdin.readline
n=int(input())
D=[*map(int,input().split())]
h=int(ceil(log2(n)))
tree=[0]*(1<<(h+1))
init(1,0,n-1)
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==1:
        D[b-1]=c
        update(1,0,n-1,b-1,c)
    else:print(Min(1,0,n-1,b-1,c-1))