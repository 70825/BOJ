N=int(input())
D=[0]+[*map(int,input().split())]
max_D=[0]*(N+1)
for i in range(1,N+1):
    for j in range(1,i+1):
        max_D[i]=max(max_D[i],max_D[i-j]+D[j])
print(max_D[N])