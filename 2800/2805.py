n,m=map(int,input().split())
D=[*map(int,input().split())]
Min,Max=0,max(D)
while Min+1<Max:
    mid=(Min+Max)//2
    ans=0
    for i in range(n):
        if D[i]>mid:ans+=D[i]-mid
    if ans>=m:Min=mid
    else:Max=mid
print(Min)