A = str(input())
B = str(input())
C = [0] * 26
D = [0] * 26
s = 0
for i in range(len(A)):
    for j in range(26):
        if A[i] == chr(j+97):
            C[j] += 1
for i in range(len(B)):
    for j in range(26):
        if B[i] == chr(j+97):
            D[j] += 1
for i in range(26):
    if C[i] > 0 and  D[i] > 0:
        s += min(C[i],D[i])
print(len(A)+len(B)-2*s)