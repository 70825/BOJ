N = int(input())
A = input().split()
B = []
for i in range(N):
    B.append(int(A[i]))
B = list(set(B))
B.sort()
for i in range(len(B)):
    print(B[i],end=" ")