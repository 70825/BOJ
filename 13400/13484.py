X=int(input())
N=int(input())
k=X*(N+1)
for i in range(N):
    k-=int(input())
print(k)