a=['a']*10;k=10;s=[0]*10;d=0
for i in range(10):
    a[i]=str(input())
    if a[i]=='':k=i;break
if k==0:print('0')
else:
    for i in range(k):
        a[i]=int(a[i])
    s[0]=int(a[0])
    if k==1:
        print(s[0])
    else:
        for i in range(1,k):
            s[i]=s[i-1]+int(a[i])
            if s[i]>=100:
                d=i
                break
        if abs(100-s[d])<=abs(100-s[d-1]):
            print(s[d])
        else:print(s[d-1])