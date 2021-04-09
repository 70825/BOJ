n,m = map(int,input().split())
a,b=abs(n),abs(m)
while b!=0:a,b=b,a%b
if a==0:print(0)
elif a==1:print(1)
else:print(2)