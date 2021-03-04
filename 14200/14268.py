def dfs(x):
    global c
    c+=1
    s[x]=c
    for nx in children[x]:
        dfs(nx)
    e[x]=c
def lazy_update(now,s,e):
    if lazy[now]==0:return
    tree[now]+=lazy[now]*(e-s+1)
    if s!=e:
        lazy[now*2]+=lazy[now]
        lazy[now*2+1]+=lazy[now]
    lazy[now]=0
def update(now,s,e,L,R,val):
    lazy_update(now,s,e)
    if s>R or e<L:return
    if L<=s and e<=R:
        lazy[now]+=val
        lazy_update(now,s,e)
        return
    mid=(s+e)//2
    update(now*2,s,mid,L,R,val)
    update(now*2+1,mid+1,e,L,R,val)
    tree[now]=tree[now*2]+tree[now*2+1]
def find(now,s,e,idx):
    lazy_update(now,s,e)
    if idx<s or idx>e:return 0
    if s==e:return tree[now]
    mid=(s+e)//2
    return find(now*2,s,mid,idx)+find(now*2+1,mid+1,e,idx)

import sys
from math import ceil,log2
sys.setrecursionlimit(500001)
input=sys.stdin.readline

n,m=map(int,input().split())
children=[[] for _ in range(n)]
D=[*map(int,input().split())]
for i in range(1,n):
    children[D[i]-1].append(i)
h=int(ceil(log2(n)))
tree=[0]*(1<<(h+1))
lazy=[0]*(1<<(h+1))
s,e=[0]*n,[0]*n
c=-1
dfs(0)
for i in range(m):
    inp=[*map(int,input().split())]
    if inp[0]==1:
        a,b=map(int,inp[1::]);a-=1
        update(1,0,n-1,s[a],e[a],b)
    else:
        a=inp[1]-1
        print(find(1,0,n-1,s[a]))