a=[*map(int,input().split())]
b=[*map(int,input().split())]
ans=0
for i in range(3):
    if b[i]-a[i]>0:ans+=b[i]-a[i]
print(ans)