N = int(input())
A = [[0]*2 for i in range(N)]
for i in range(N):
    A[i][1],A[i][0] = map(int,input().split())
A.sort()
for i in range(N):
    print(A[i][1],A[i][0])