A,B = map(int,input().split())
N = [[0]*B for i in range(A)]
M = [[0]*B for i in range(A)]
for i in range(A):
    C = input().split()
    for j in range(B):
        N[i][j] = int(C[j])
for i in range(A):
    C = input().split()
    for j in range(B):
        M[i][j] = int(C[j])
for i in range(A):
    for j in range(B):
        print(N[i][j]+M[i][j],end=" ")
    print("")