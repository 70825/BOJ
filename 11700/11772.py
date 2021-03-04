N=int(input())
D=[0]*N
for i in range(N):
    S=str(input())
    D[i]=int((S[:len(S)-1:]))**int((S[len(S)-1::]))
print(sum(D))