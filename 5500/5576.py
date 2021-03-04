A=[0]*10;B=[0]*10
for i in range(10):
    A[i]=int(input())
for i in range(10):
    B[i]=int(input())
A.sort()
B.sort()
print(A[9]+A[8]+A[7],B[9]+B[8]+B[7])