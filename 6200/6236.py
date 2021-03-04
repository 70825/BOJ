n,m=map(int,input().split())
D=[int(input()) for i in range(n)]
Min,Max=0,sum(D)
k=float('inf')
while Min<=Max:
    mid=(Min+Max)//2
    ans=0;z=0;s=0
    for i in range(n):
        if ans+D[i]<=mid: ans+=D[i]
        else:s=max(s,ans);ans=D[i];z+=1
    z+=1
    if z<=m: k=min(k,max(s,ans));Max=mid-1
    else: Min=mid+1
print(k)