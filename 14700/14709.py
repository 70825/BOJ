err=0
x,y,z=0,0,0
for i in range(int(input())):
    a,b=map(int,input().split())
    D=[min(a,b),max(a,b)]
    if D==[1,3]:x+=1
    elif D==[1,4]:y+=1
    elif D==[3,4]:z+=1
    else:err+=1
if err==0 and min(x,y,z)>=1:print('Wa-pa-pa-pa-pa-pa-pow!')
else:print('Woof-meow-tweet-squeek')