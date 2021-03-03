R,C,ZR,ZC = map(int,input().split())
A = [["A"]*C for i in range(R)]
for i in range(R):
    B = str(input())
    for j in range(C):
        A[i][j] = B[j]
for i in range(R*ZR):
    for j in range(C*ZC):
        print(A[i//ZR][j//ZC],end="")
    print("")