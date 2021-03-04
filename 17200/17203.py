N,Q=map(int,input().split())
a=[0]+[*map(int,input().split())]
for i in range(Q):
    ans=0
    l,r=map(int,input().split())
    for j in range(l,r):ans+=abs(a[j+1]-a[j])
    print(ans)