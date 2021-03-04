N=int(input())
S=str(input())
D=[0]*26
for i in range(N):D[ord(S[i])-97]+=1
for i in range(26):
    if D[i]==max(D):
        print(chr(i+97),D[i])