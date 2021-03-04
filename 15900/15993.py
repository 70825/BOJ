D=[[0]*2 for _ in range(100001)]
MOD=10**9+9
D[1][0]=1
D[2]=[1,1]
D[3]=[2,2]
for i in range(4,100001):
    D[i][1]=(D[i-1][0]+D[i-2][0]+D[i-3][0])%MOD
    D[i][0]=(D[i-1][1]+D[i-2][1]+D[i-3][1])%MOD
for _ in range(int(input())):
    print(*D[int(input())])