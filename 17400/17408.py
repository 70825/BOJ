def init(now,s,e):
    if s==e:
        tree[now]=[D[s],0]
        return tree[now]
    mid=(s+e)//2
    z=sorted(init(now*2,s,mid)+init(now*2+1,mid+1,e))
    tree[now]=[z[-1],z[-2]]
    return tree[now]
def update(now,s,e,idx,val):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]=[val,0]
        return tree[now]
    mid=(s+e)//2
    z=sorted(update(now*2,s,mid,idx,val)+update(now*2+1,mid+1,e,idx,val))
    tree[now]=[z[-1],z[-2]]
    return tree[now]
def find(now,s,e,L,R):
    if s>R or e<L:return [0,0]
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    z=sorted(find(now*2,s,mid,L,R)+find(now*2+1,mid+1,e,L,R))
    return [z[-1],z[-2]]

input=__import__('sys').stdin.readline
from math import ceil,log2
n=int(input())
D=[*map(int,input().split())]
h=int(ceil(log2(n+1)))
tree=[0]*(1<<(h+1))
init(1,0,n-1)
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==1:update(1,0,n-1,b-1,c)
    else:print(sum(find(1,0,n-1,b-1,c-1)))