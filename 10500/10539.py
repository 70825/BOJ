N = int(input())
A = input().split()
for i in range(N):
    A[i] = int(A[i])
print(A[0],end=" ")
if N == 1:
    print("")
else:
    for i in range(1,N):
        print(A[i]*(i+1)-A[i-1]*i,end=" ")
    print("")