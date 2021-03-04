D=[0,0]
t,ans=1,0
n=int(input())
def k(x):
    if x==n:print(*D);exit()
    else:return
for i in range(n):
    if i%4==0:
        for j in range(t):D[1]+=1;ans+=1;k(ans)
    if i%4==1:
        for j in range(t):D[0]+=1;ans+=1;k(ans)
        t+=1
    if i%4==2:
        for j in range(t):D[1]-=1;ans+=1;k(ans)
    if i%4==3:
        for j in range(t):D[0]-=1;ans+=1;k(ans)
        t+=1