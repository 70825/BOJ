D=[0]*100001
MOD=10**9+9
D[0]=1;D[1]=1;D[2]=2;D[3]=2
for i in range(4,100001):
    D[i]=(D[i-2]+D[i-4]+D[i-6])%MOD
for _ in range(int(input())):
    print(D[int(input())]%MOD)