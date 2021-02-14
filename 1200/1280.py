from math import ceil,log2
input=__import__('sys').stdin.readline

class segment():
    def __init__(self,x):
        self.h=int(ceil(log2(x)))
        self.tree=[0]*(1<<(self.h+1))
    def update(self,now,s,e,idx,val):
        if s>idx or e<idx:return self.tree[now]
        if s==e:
            self.tree[now]=(self.tree[now]+val)%MOD
            return self.tree[now]
        mid=(s+e)//2
        self.tree[now]=(self.update(now*2,s,mid,idx,val)%MOD+self.update(now*2+1,mid+1,e,idx,val)%MOD)%MOD
        return self.tree[now]
    def Find(self,now,s,e,L,R):
        if s>R or e<L:return 0
        if L<=s and e<=R:return self.tree[now]
        mid=(s+e)//2
        return (self.Find(now*2,s,mid,L,R)%MOD+self.Find(now*2+1,mid+1,e,L,R)%MOD)%MOD

MAX=200000
MOD=10**9+7
ST_sum=segment(MAX+1)
ST_cnt=segment(MAX+1)
ans=1
for i in range(int(input())):
    k=int(input())
    ST_sum.update(1,0,MAX,k,k)
    ST_cnt.update(1,0,MAX,k,1)
    if i==0:continue
    a=(ST_cnt.Find(1,0,MAX,0,k-1)*k-ST_sum.Find(1,0,MAX,0,k-1))%MOD
    b=(ST_sum.Find(1,0,MAX,k+1,MAX)-ST_cnt.Find(1,0,MAX,k+1,MAX)*k)%MOD
    ans=(ans*(a+b))%MOD
print(ans)