D=[[0]*4 for _ in range(100001)]
MOD=10**9+9
D[1][1]=1;D[2][2]=1
D[3]=[0,1,1,1]
for i in range(4,100001):
    D[i][1]=(D[i-1][2]+D[i-1][3])%MOD
    D[i][2]=(D[i-2][1]+D[i-2][3])%MOD
    D[i][3]=(D[i-3][1]+D[i-3][2])%MOD
for _ in range(int(input())):
    print(sum(D[int(input())])%MOD)