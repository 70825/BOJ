a,b,c=map(int,input().split())
ans=1
while b:
    if b%2==1:ans=(ans*a)%c
    b//=2;a=(a**2)%c
print(ans)