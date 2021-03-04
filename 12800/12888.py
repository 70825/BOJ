h=int(input())
ans=0
if h%2==1:
    for i in range(0,h,2):
        ans+=2**i
else:
    ans+=1
    for i in range(1,h,2):
        ans+=2**i
print(ans)