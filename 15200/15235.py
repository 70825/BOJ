import sys
N=int(input())
A=sys.stdin.readline().split()
for i in range(len(A)):A[i]=int(A[i])
n=0;a=[0]*len(A)
for i in range(len(A)*max(A)):
    if A[i%len(A)]>0:
        A[i%len(A)]-=1
        a[i%len(A)]=n+1
        n+=1
for i in range(N):
    print(a[i],end=" ")