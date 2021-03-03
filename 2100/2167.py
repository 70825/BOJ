import sys
N,M = map(int,input().split())
A = [[0]*M for i in range(N)]
for i in range(N):
    B = sys.stdin.readline().split()
    for j in range(M):
        A[i][j] = int(B[j])
T = int(input())
for i in range(T):
    a,b,c,d = map(int,sys.stdin.readline().split())
    s = 0
    for j in range(b-1,d):
        for k in range(a-1,c):
            s += A[k][j]
    print(s)