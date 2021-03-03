a,b=map(int,input().split())
x=(a+b)//2;y=(a-b)//2
if y>=0 and x+y==a and x-y==b:print(x,y)
else:print(-1)