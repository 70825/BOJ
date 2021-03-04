x=[];y=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    x.append(a);y.append(b)
print(max(max(y)-min(y),max(x)-min(x))**2)