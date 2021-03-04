A = str(input())
B = str(input())
d = 0
for i in range(len(A)-len(B)+1):
    s = 0
    for j in range(len(B)):
        if A[i+j] == B[j]:
            s += 1
    if s == len(B):
        d += 1
print(d)