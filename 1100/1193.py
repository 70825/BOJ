N=int(input())
z=0;k=1
while z<=N:
    z+=k
    if z>=N:break
    k+=1
x=z-N
if k%2==1:print(str(1+x)+'/'+str(k-x))
else:print(str(k-x)+'/'+str(1+x))