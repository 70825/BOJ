A = [0] * 10
B = []
for i in range(10):
    A[i] = int(input())
    B.append(A[i])
print(sum(A)//10)
B = list(set(B))
C = [0] * len(B)
for i in range(10):
    for j in range(len(C)):
        if A[i] == B[j]:
            C[j] += 1
for i in range(len(C)):
    if C[i] == max(C):
        print(B[i])