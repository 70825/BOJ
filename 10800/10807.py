N=int(input())
A=input().split()
B=str(input())
C=0
for i in range(len(A)):
    if A[i] == B:
        C+=1
print(C)