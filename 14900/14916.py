n=int(input());s=0
while n!=0:
    if n>=14:n-=10;s+=2
    elif n==13:n-=13;s+=1+4
    elif n==12:n-=12;s+=2+1
    elif n==11:n-=11;s+=1+3
    elif n==10:n-=10;s+=2
    elif n==9:n-=9;s+=1+2
    elif n==8:n-=8;s+=4
    elif n==7:n-=7;s+=1+1
    elif n==6:n-=6;s+=3
    elif n==5:n-=5;s+=1
    elif n==4:n-=4;s+=2
    elif n==3:break
    elif n==2:n-=2;s+=1
    elif n==1:break
if n>0:print(-1)
else:print(s)