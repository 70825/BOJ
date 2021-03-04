K=str(input())
s=0
for i in range(len(K)):
    if K[i]=='*':k=i
    elif i%2==0:s+=int(K[i])
    else:s+=3*int(K[i])
if s%10==0:print(0)
elif k%2==0:
    q=s//10+1
    print(q*10-s)
else:
    q=s//10+1
    if (q*10-s)%3==0:
        print((q*10-s)//3)
    elif (10*(q+1)-s)%3==0:
        print((10*(q+1)-s)//3)
    else:
        print((10*(q+2)-s)//3)