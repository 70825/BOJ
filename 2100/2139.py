Year=[31,28,31,30,31,30,31,31,30,31,30,31]
Leap_Year=[31,29,31,30,31,30,31,31,30,31,30,31]
memo=[1700,1800,1900,2100,2200]
while 1:
    d,m,y=map(int,input().split())
    if d==m==y==0:break
    ans=0
    if y%4==0 and y not in memo:
        for i in range(m-1):ans+=Leap_Year[i]
    else:
        for i in range(m-1):ans+=Year[i]
    ans+=d
    print(ans)