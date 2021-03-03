d = 0
A = str(input())
for i in range(len(A)):
    d += int(A[i],16)*16**(len(A)-i-1)
print(d)