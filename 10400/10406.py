W,N,P=map(int,input().split())
D=[*map(int,input().split())]
ans=0
for i in range(P):
    if W<=D[i]<=N:ans+=1
print(ans)