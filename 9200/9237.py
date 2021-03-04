N=int(input())
D=sorted([*map(int,input().split())],reverse=True)
k=1
for i in range(N):
    if (i+1)+D[i]>k:k=(i+1)+D[i]
print(k+1)