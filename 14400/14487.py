import sys
T=int(input())
A=sys.stdin.readline().split()
for i in range(len(A)):
    A[i]=int(A[i])
print(sum(A)-max(A))