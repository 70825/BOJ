n,m=map(int,input().split())
D=[*map(int,input().split())]
Min,Max=0,sum(D)
k=float('inf')
while Min<=Max:
    mid=(Min+Max)//2
    K=[0]*m
    ans=0;z=0;s=0
    for i in range(n):
        if ans+D[i]<=mid:ans+=D[i]
        else:z=max(z,ans);ans=D[i];s+=1
    s+=1
    if s<=m:k=min(k,max(z,ans));Max=mid-1
    else:Min=mid+1
print(k)