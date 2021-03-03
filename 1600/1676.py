N = int(input())
A = 1
c = 0
for i in range(2,N+1,1):
    A *= i
A = str(A)
for i in range(len(A)-1,-1,-1):
    if A[i] == '0':
        c += 1
    else:
        print(c)
        break