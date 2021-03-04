N=int(input())
D=[*map(int,input().split())]
S=[1]*N
for i in range(N):
    for j in range(i):
        if D[i]<D[j]:S[i]=max(S[i],S[j]+1)
print(max(S))