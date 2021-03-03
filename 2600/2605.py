N = int(input())
A = input().split()
B = []
for i in range(N):
    A[i]=int(A[i])
    B.insert(A[i],i+1)
for i in range(N):
    print(B[N-i-1],end=" ")