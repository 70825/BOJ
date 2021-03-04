N=int(input())
a=0;b=0;c=0;k=0
while N!=0:
    if N>=300:N-=300;a+=1
    elif N>=60:N-=60;b+=1
    else:N-=10;c+=1
    if N<0:k=1;break
if k==0:print(a,b,c)
else:print(-1)