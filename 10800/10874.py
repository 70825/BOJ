N = int(input())
A = [[0] * 10 for i in range(N)]
score = [0] * N
for i in range(N):
    B = input()
    A[i] = B.split()
    if int(max(A[i])) <= 5 and int(min(A[i])) >= 1:
        for j in range(10):
            A[i][j] = int(A[i][j])
    for j in range(10):
        if A[i][j] == j%5 + 1:
            score[i] += 1
    if score[i] == 10:
        print(i+1)