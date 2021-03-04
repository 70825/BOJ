input()
D=sorted([*map(int,input().split())])
k=sum(D)
ans=0
for i in range(len(D)-1):
    k-=D[i]
    ans+=D[i]*k
print(ans)