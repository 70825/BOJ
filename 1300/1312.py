a,b,n=map(int,input().split())
a-=a//b*b;a*=10
for i in range(n):k=a//b;a-=k*b;a*=10
print(k)