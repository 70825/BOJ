def update(now,s,e,idx,val):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]=val
        return tree[now]
    tree[now]=update(now*2,s,(s+e)//2,idx,val)+update(now*2+1,(s+e)//2+1,e,idx,val)
    return tree[now]
def Sum(now,s,e,L,R):
    if s>R or e<L:return 0
    if L<=s and e<=R:return tree[now]
    return (Sum(now*2,s,(s+e)//2,L,R))+Sum(now*2+1,(s+e)//2+1,e,L,R)
from math import ceil,log2
input=__import__('sys').stdin.readline
n,q=map(int,input().split())
h=int(ceil(log2(n)))
D=[0]*n
tree=[0]*(1<<(h+1))
for i in range(q):
    a,b,c=map(int,input().split())
    b-=1
    if a==1:
        D[b]+=c
        update(1,0,n-1,b,D[b])
    else:print(Sum(1,0,n-1,b,c-1))