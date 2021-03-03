n=input()
D=[]
for i in range(len(n)):
    D.append(int(n[i]))
l,r,mid=0,1,0
ans=0
for i in range(len(D)):
    s,mid,e=i,i,i+1
    while s!=-1 and e!=len(n):
        if sum(D[s:mid+1])==sum(D[mid+1:e+1]):
            ans=max(ans,(e-mid)*2)
        s-=1;e+=1
print(ans)