N = int(input())
S = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a = 0
for i in range(N):
    A = str(input())
    for j in range(26):
        if chr(j+97) == A[0]:
            S[j] += 1
for i in range(26):
    if S[i] >= 5:
        print(chr(i+97),end="")
        a += 1
if a == 0:
    print("PREDAJA")