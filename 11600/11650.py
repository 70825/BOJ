N = int(input())
A = [[0]*2 for i in range(N)]
for i in range(N):
    A[i][0],A[i][1] = map(int,input().split())
A.sort()
for i in range(N):
    print(A[i][0],A[i][1])