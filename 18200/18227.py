def dfs(x,z):
    global cnt
    cnt+=1
    pre[x]=cnt
    deep[x]=z
    for nx in child[x]:
        if pre[nx]==-1:dfs(nx,z+1)
    post[x]=cnt
def update(now,s,e,idx):
    if s>idx or e<idx:return tree[now]
    if s==e:
        tree[now]+=1
        return tree[now]
    mid=(s+e)//2
    tree[now]=update(now*2,s,mid,idx)+update(now*2+1,mid+1,e,idx)
    return tree[now]
def PRINT(now,s,e,L,R):
    if s>R or e<L:return 0
    if L<=s and e<=R: return tree[now]
    mid=(s+e)//2
    return PRINT(now*2,s,mid,L,R)+PRINT(now*2+1,mid+1,e,L,R)
import sys
sys.setrecursionlimit(500000)
input=sys.stdin.readline
from math import ceil,log2
n,c=map(int,input().split())
h=int(ceil(log2(n)))
child=[[] for _ in range(n)]
pre=[-1]*n
post=[-1]*n
deep=[-1]*n
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1;b-=1
    child[a].append(b)
    child[b].append(a)
cnt=-1
dfs(c-1,1)
tree=[0]*(1<<(h+1))
for i in range(int(input())):
    a,b=map(int,input().split());b-=1
    if a==1:update(1,0,n-1,pre[b])
    else:print(PRINT(1,0,n-1,pre[b],post[b])*deep[b])