a=int(input())
d=[0,0,1,1]
for i in range(4,a+1):
    d.append(d[i-1]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
print(d[a])