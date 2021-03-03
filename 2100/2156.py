N=int(input());S=[0]
for i in range(N):S.append(int(input()))
D=[[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    D[i][0]=max(D[i-1][0],D[i-1][1],D[i-1][2])
    D[i][1]=D[i-1][0]+S[i]
    D[i][2]=D[i-1][1]+S[i]
print(max(D[N]))