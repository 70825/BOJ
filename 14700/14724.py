N = int(input())
A = [[0] * N for i in range(9)]
C = [0] * 9
D = ["PROBRAIN","GROW","ARGOS","ADMIN","ANT","MOTION","SPG","COMON","ALMIGHTY"]
for i in range(9):
    B = input().split()
    for j in range(N):
        A[i][j] = int(B[j])
    C[i] = max(A[i])
for i in range(9):
    if max(C) == C[i]:
        print(D[i])