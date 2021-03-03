D=[[0]*2 for _ in range(91)];D[1][1]=1
N=int(input())
for i in range(2,N+1):
    D[i][1]+=D[i-1][0]
    D[i][0]+=D[i-1][0]+D[i-1][1]
print(sum(D[N]))