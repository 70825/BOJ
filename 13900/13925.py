def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    mid=(s+e)//2
    tree[now]=(init(now*2,s,mid)+init(now*2+1,mid+1,e))%MOD
    return tree[now]
def lazy_update(now,s,e):
    if sum_lazy[now]==0 and mul_lazy[now]==1:return
    tree[now]=(tree[now]*mul_lazy[now]+(e-s+1)*sum_lazy[now])%MOD
    if s!=e:
        for i in range(now*2,now*2+2):
            sum_lazy[i]=(sum_lazy[i]*mul_lazy[now]+sum_lazy[now])%MOD
            mul_lazy[i]=(mul_lazy[i]*mul_lazy[now])%MOD
    mul_lazy[now]=1
    sum_lazy[now]=0
def update(now,s,e,L,R,Sum,Mul):
    lazy_update(now,s,e)
    if L>e or s>R:return tree[now]
    if L<=s and e<=R:
        sum_lazy[now]=(sum_lazy[now]*Mul+Sum)%MOD
        mul_lazy[now]=(mul_lazy[now]*Mul)%MOD
        lazy_update(now,s,e)
        return tree[now]
    mid=(s+e)//2
    tree[now]=(update(now*2,s,mid,L,R,Sum,Mul)+update(now*2+1,mid+1,e,L,R,Sum,Mul))%MOD
    return tree[now]
def Sum(now,s,e,L,R):
    lazy_update(now,s,e)
    if L>e or R<s:return 0
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return (Sum(now*2,s,mid,L,R)+Sum(now*2+1,mid+1,e,L,R))%MOD

from math import ceil,log2
input=__import__('sys').stdin.readline
MOD=10**9+7
n=int(input())
h=int(ceil(log2(n)))
tree=[0]*(1<<(h+1))
sum_lazy=[0]*(1<<(h+1))
mul_lazy=[1]*(1<<(h+1))
D=[*map(int,input().split())]
init(1,0,n-1)
for i in range(int(input())):
    inp=[*map(int,input().split())]
    if inp[0]==4:
        a,b,c=inp
        print(Sum(1,0,n-1,b-1,c-1))
    else:
        a,b,c,d=inp;b-=1;c-=1
        if a==1:update(1,0,n-1,b,c,d,1)
        if a==2:update(1,0,n-1,b,c,0,d)
        if a==3:update(1,0,n-1,b,c,d,0)