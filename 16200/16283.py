a,b,n,w=map(int,input().split())
x,y,ax,ay,t=n-1,1,0,0,0
if a*x+b*y==w:ax,ay=x,y;t+=1
for i in range(n-2):
    x-=1;y+=1
    if a*x+b*y==w:ax,ay=x,y;t+=1
if t==1:print(ax,ay)
else:print(-1)