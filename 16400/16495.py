S=str(input())
k=0
for i in range(len(S)):
    k+=(ord(S[i])-64)*26**(len(S)-1-i)
print(k)