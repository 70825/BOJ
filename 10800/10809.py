S = str(input())
A = [-1] * 26
for i in range(len(S)):
    for j in range(26):
        if S[i] == chr(j+97):
            if A[j] >= 0:
                break
            A[j] = i
for i in range(26):
    print(A[i],end=" ")