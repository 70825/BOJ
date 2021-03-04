from decimal import Decimal
n,m=map(int,input().split())
A=input().split()
for u in range(n):
    A[u]=Decimal(A[u])
for i in range(m):
    A.sort()
    q=A[0]+A[1]
    A[0]=q;A[1]=q
print(sum(A))