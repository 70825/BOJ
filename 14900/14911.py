a=list(map(int,input().split()))
b=int(input())
a.sort()
D=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==b:
            D.append([a[i],a[j]])
d=[]
if len(D)!=0:
    d.append(D[0])
    for i in range(1,len(D)):
        if d[-1] != D[i]:
            d.append(D[i])
for i in d:
    print(i[0],i[1])
print(len(d))