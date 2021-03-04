N,M=map(int,input().split())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
C=A+B
C.sort()
for i in range(N+M):
    print(C[i],end=" ")