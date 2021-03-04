D=[[0]*1001 for _ in range(1001)]
MOD=10**9+9
D[1][1]=1;D[2][1]=1;D[2][2]=1
D[3][1]=1;D[3][2]=2;D[3][3]=1
for i in range(4,1001):
    for j in range(2,i+1):
        D[i][j]=(D[i-1][j-1]+D[i-2][j-1]+D[i-3][j-1])%MOD
for _ in range(int(input())):
    n,m=map(int,input().split())
    print(sum(D[n][:m+1])%MOD)