def D(N):
    return 3*N*(N+1)//2
N=int(input())
ans=0
for i in range(N):
    ans+=D(i+1)
print(ans)