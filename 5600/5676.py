def update(now,s,e,idx,val):
    if idx<s or idx>e:return tree[now]
    if s==e:
        tree[now]=val
        return tree[now]
    mid=(s+e)//2
    tree[now]=update(now*2,s,mid,idx,val)*update(now*2+1,mid+1,e,idx,val)
    return tree[now]
def mul(now,s,e,L,R):
    if s>R or e<L:return 1
    if L<=s and e<=R:return tree[now]
    mid=(s+e)//2
    return mul(now*2,s,mid,L,R)*mul(now*2+1,mid+1,e,L,R)
input=__import__('sys').stdin.readline
from math import ceil,log2
while 1:
    inp=input().split()
    if not inp:break
    n,k=map(int,inp)
    h=int(ceil(log2(n)))
    D=[*map(int,input().split())]
    tree=[0]*(1<<(h+1))
    for i in range(n):
        if D[i]>0:update(1,0,n-1,i,1)
        elif D[i]<0:update(1,0,n-1,i,-1)
        else:update(1,0,n-1,i,0)
    for i in range(k):
        a,b,c=input().split()
        b=int(b);c=int(c)
        if a=='C':update(1,0,n-1,b-1,1) if c>0 else update(1,0,n-1,b-1,-1) if c<0 else update(1,0,n-1,b-1,0)
        else:
            k=mul(1,0,n-1,b-1,c-1)
            print('+',end='') if k==1 else print('-',end='') if k==-1 else print(0,end='')
    print()