def init(now,s,e):
    if s==e:
        tree[now]+=[D[s]]
        return tree[now]
    mid=(s+e)//2
    tree[now]+=init(now*2,s,mid)+init(now*2+1,mid+1,e)
    return tree[now]
def upper(now,s,e,L,R,k):
    if s>R or e<L:return 0;
    if L<=s and e<=R:return len(tree[now])-bisect(tree[now],k)
    mid=(s+e)//2
    return upper(now*2,s,mid,L,R,k)+upper(now*2+1,mid+1,e,L,R,k)
input=__import__('sys').stdin.readline
from math import ceil,log2
from bisect import bisect
n=int(input())
h=int(ceil(log2(n)))
tree=[[] for _ in range(1<<(h+1))]
D=[*map(int,input().split())]
init(1,0,n-1)
for i in range(len(tree)):
    tree[i]=sorted(tree[i])
for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(upper(1,0,n-1,a-1,b-1,c))