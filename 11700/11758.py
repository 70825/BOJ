x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a1,b1,a2,b2=x2-x1,y2-y1,x3-x1,y3-y1
c=a1*b2-a2*b1
print(1) if c>0 else print(-1) if c<0 else print(0)