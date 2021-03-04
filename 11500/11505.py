def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    else:
        tree[now]=(init(now*2,s,(s+e)//2)*init(now*2+1,(s+e)//2+1,e))%MOD
        return tree[now]
def mul(now,s,e,L,R):
    if s>R or e<L:return 1
    if L<=s and e<=R:return tree[now]
    return ((mul(now*2,s,(s+e)//2,L,R))*mul(now*2+1,(s+e)//2+1,e,L,R))%MOD
def update(now,s,e,idx,nx):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]=nx
        return tree[now]
    tree[now]=(update(now*2,s,(s+e)//2,idx,nx)*update(now*2+1,(s+e)//2+1,e,idx,nx))%MOD
    return tree[now]
input=__import__('sys').stdin.readline
MOD=10**9+7
n,m,k=map(int,input().split())
D=[int(input()) for i in range(n)]
tree=[1]*(4*n)
init(1,0,n-1)
for i in range(m+k):
    a,b,c=map(int,input().split())
    b-=1
    if a==1:update(1,0,n-1,b,c)
    else:print(mul(1,0,n-1,b,c-1))