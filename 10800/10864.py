N,M=map(int,input().split())
D=[[] for i in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    D[A-1].append(B)
    D[B-1].append(A)
for i in range(N):
    print(len(D[i]))