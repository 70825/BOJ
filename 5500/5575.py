for i in range(3):
    h=[0]*2;m=[0]*2;s=[0]*2;H=0;M=0;S=0
    h[0],m[0],s[0],h[1],m[1],s[1]=map(int,input().split())
    if s[1]-s[0]<0:m[1]-=1;S=60+s[1]-s[0]
    else:S=s[1]-s[0]
    if m[1]-m[0]<0:h[1]-=1;M=60+m[1]-m[0]
    else:M=m[1]-m[0]
    if h[1]-h[0]<0:H=24+h[1]-h[0]
    else:H=h[1]-h[0]
    print(H,M,S)