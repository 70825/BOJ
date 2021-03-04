from math import gcd
n,s=map(int,input().split())
D=[*map(int,input().split())]
for i in range(n):
    D[i]=abs(s-D[i])
if n==1:print(D[0]);exit()
ans=gcd(D[0],D[1])
for i in range(2,n):
    ans=gcd(ans,D[i])
print(ans)