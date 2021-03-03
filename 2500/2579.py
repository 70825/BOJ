N=int(input())
D=[0]*(N+1)
S=[[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    D[i]=int(input())
S[1][1]=D[1]
for i in range(2,N+1):
    S[i][1]=max(S[i-2][1],S[i-2][2])+D[i]
    S[i][2]=S[i-1][1]+D[i]
print(max(S[N]))