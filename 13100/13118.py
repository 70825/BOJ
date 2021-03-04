p=[0]*4;r=-1
p[0],p[1],p[2],p[3]=map(int,input().split())
x,y,q=map(int,input().split())
for i in range(4):
    if x==p[i]:r=i+1
if r==-1:print(0)
else:print(r)