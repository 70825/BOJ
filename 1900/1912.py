N=int(input())
D=[*map(int,input().split())]
S=[0]*N;S[0]=D[0]
for i in range(1,N):S[i]=max(D[i],S[i-1]+D[i])
print(max(S))