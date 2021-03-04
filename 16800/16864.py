a,b,c=map(float,input().split())
a=int(100*a+0.5);b=int(100*b+0.5);c=int(100*c+0.5)
D=[]
i=0
while a-b*i>=0:
    if (a-b*i)%c==0:D.append((i,(a-b*i)//c))
    i+=1
if len(D)==0:print('none')
else:
    for i in range(len(D)):
        print(D[i][0],D[i][1])