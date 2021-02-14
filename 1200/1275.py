def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    tree[now]=init(now*2,s,(s+e)//2)+init(now*2+1,(s+e)//2+1,e)
    return tree[now]
def Sum(now,s,e,L,R):
    if s>R or e<L:return 0
    if L<=s and e<=R:return tree[now]
    return Sum(now*2,s,(s+e)//2,L,R)+Sum(now*2+1,(s+e)//2+1,e,L,R)
def update(now,s,e,idx,val):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]+=val
        return tree[now]
    tree[now] = update(now*2,s,(s+e)//2,idx,val)+update(now*2+1,(s+e)//2+1,e,idx,val)
    return tree[now]

from math import ceil,log2
input=__import__('sys').stdin.readline
n,q=map(int,input().split())
h=int(ceil(log2(n)))
D=[*map(int,input().split())]
tree=[0]*(1<<(h+1))
init(1,0,n-1)
for i in range(q):
    x,y,a,b=map(int,input().split())
    x-=1;y-=1;a-=1
    print(Sum(1,0,n-1,min(x,y),max(x,y)))
    val=b-D[a]
    D[a]=b
    update(1,0,n-1,a,val)