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
def yaza_lazy_update(now,s,e):
    if yaza_lazy[now]==0:return
    yaza_tree[now]+=yaza_lazy[now]*(e-s+1)
    if s!=e:
        yaza_lazy[now*2]+=yaza_lazy[now]
        yaza_lazy[now*2+1]+=yaza_lazy[now]
    yaza_lazy[now]=0
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
def yaza_update(now,s,e,L,R,val):
    yaza_lazy_update(now,s,e)
    if s>R or e<L:return
    if L<=s and e<=R:
        yaza_lazy[now]+=val
        yaza_lazy_update(now,s,e)
        return
    mid=(s+e)//2
    yaza_update(now*2,s,mid,L,R,val)
    yaza_update(now*2+1,mid+1,e,L,R,val)
    yaza_tree[now]=yaza_tree[now*2]+yaza_tree[now*2+1]
def find(now,s,e,L,R):
    lazy_update(now,s,e)
    if R<s or L>e:return 0
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return find(now*2,s,mid,L,R)+find(now*2+1,mid+1,e,L,R)
def yaza_find(now,s,e,L,R):
    yaza_lazy_update(now,s,e)
    if R<s or L>e:return 0
    if L<=s and e<=R:return yaza_tree[now]
    mid=(s+e)//2
    return yaza_find(now*2,s,mid,L,R)+yaza_find(now*2+1,mid+1,e,L,R)

import sys
from math import ceil,log2
sys.setrecursionlimit(100001)
input=sys.stdin.readline

n,m=map(int,input().split())
children=[[] for _ in range(n)]
D=[*map(int,input().split())]
for i in range(1,n):
    children[D[i]-1].append(i)
h=int(ceil(log2(n)))
time=0
yaza_tree=[0]*(1<<(h+1))
yaza_lazy=[0]*(1<<(h+1))
tree=[0]*(1<<(h+1))
lazy=[0]*(1<<(h+1))
s,e=[0]*n,[0]*n
c=-1
dfs(0)
for i in range(m):
    inp=[*map(int,input().split())]
    if inp[0]==1:
        a,b=map(int,inp[1::]);a-=1
        if time==0:update(1,0,n-1,s[a],e[a],b)
        else:yaza_update(1,0,n-1,s[a],s[a],b)
    elif inp[0]==2:
        a=inp[1]-1
        print(find(1,0,n-1,s[a],s[a])+yaza_find(1,0,n-1,s[a],e[a]))
    else:time^=1