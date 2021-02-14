def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    mid=(s+e)//2
    tree[now]=max(init(now*2,s,mid),init(now*2+1,mid+1,e))
    return tree[now]
def Max(now,s,e,L,R):
    if s>R or e<L:return 0
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return max(Max(now*2,s,mid,L,R),Max(now*2+1,mid+1,e,L,R))
from math import log2,ceil
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[*map(int,input().split())]
h=int(ceil(log2(n)))
tree=[0]*(1<<(h+1))
init(1,0,n-1)
res=[]
for i in range(m-1,n-m+1):
    a=max(0,i-m+1);b=min(n-1,i+m-1)
    res+=[Max(1,0,n-1,a,b)]
print(*res)