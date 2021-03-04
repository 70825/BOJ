N=int(input())
D=[*map(int,input().split())]
ans=10**9
for i in range(1,N):
    if abs(D[i]-D[i-1])<ans:ans=abs(D[i]-D[i-1])
print(ans)