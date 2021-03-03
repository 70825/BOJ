A,B,V=map(int,input().split());k=0;s=0
V=V-A;c=A-B
if V%(A-B)==0:print(V//c+1)
else:print(V//c+2)