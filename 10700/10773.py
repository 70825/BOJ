N = int(input())
A =[]
for i in range(N):
    B = int(input())
    if B == 0:
        del A[len(A)-1]
    else:
        A.append(B)
print(sum(A))