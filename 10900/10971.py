def permutation(D):
    i=len(D)-1
    while D[i-1]>=D[i]:
        i-=1
    if i<=0:
        return False
    j=len(D)-1
    while D[i-1]>=D[j]:
        j-=1
    D[i-1],D[j]=D[j],D[i-1]
    j=len(D)-1
    while i<j:
        D[i],D[j]=D[j],D[i]
        i+=1;j-=1
    return True

N=int(input())
D=[i for i in range(N)]
cost=[];ans=10*10**6
for i in range(N):
    cost.append([*map(int,input().split())])
while 1:
    if D[0]!=0:break
    err,k,p=0,0,cost[D[N-1]][D[0]]
    if p==0:break
    else:k+=p
    for i in range(N-1):
        p=cost[D[i]][D[i+1]]
        if p==0:err=1;break
        k+=p
    if err==0 and ans>k:ans=k
    permutation(D)
print(ans)