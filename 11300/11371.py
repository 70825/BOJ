from math import *
while 1:
    a,b=map(int,input().split())
    if a==b==0:break
    if a==0:T=float('inf')
    elif b==0:T=0
    else:T=b/a
    print(round(degrees(atan(T))))