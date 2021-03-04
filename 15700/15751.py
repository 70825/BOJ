a,b,x,y=map(int,input().split())
a,b=min(a,b),max(a,b)
x,y=min(x,y),max(x,y)
print(min(abs(a-x)+abs(b-y),abs(b-a)))