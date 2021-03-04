N=int(input())
D=sorted([*map(int,input().split())])
ans=0
def permutation(N,D):
    i=N-1
    while D[i-1]>=D[i]:i-=1
    if i<=0:return False
    j=N-1
    while D[i-1]>=D[j]:j-=1
    D[i-1],D[j]=D[j],D[i-1]
    j=N-1
    while i<j:
        D[i],D[j]=D[j],D[i]
        i+=1;j-=1
    return True
while 1:
    if permutation(N,D):
        k=0
        for i in range(1,len(D)):
            k+=abs(D[i-1]-D[i])
        if k>ans:ans=k
    else:break
print(ans)