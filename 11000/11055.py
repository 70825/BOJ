N=int(input())
D=[*map(int,input().split())]
S=[0]*N
for i in range(N):
    S[i]=D[i]
    for j in range(i):
        if D[i]>D[j]:S[i]=max(S[i],S[j]+D[i])
print(max(S))