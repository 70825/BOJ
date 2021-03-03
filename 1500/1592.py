N,M,L=map(int,input().split())
D=[0]*N
k=0;ans=0
while max(D)!=M:
    D[k]+=1;ans+=1
    if max(D)%2==1:
        k+=L
        if k>N-1:k-=N
    else:
        k-=L
        if k<0:k+=N
print(ans-1)