n=int(input())
D=[*map(int,input().split())]
m=int(input())
Min,Max=0,max(D)
while Min<=Max:
    mid=(Min+Max)//2
    ans=0
    for i in range(n):
        ans+=min(mid,D[i])
    if ans<=m:Min=mid+1
    else:Max=mid-1
print((Min+Max)//2)