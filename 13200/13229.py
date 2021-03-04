import sys
N=int(input());M=[0]*N
A=sys.stdin.readline().split()
M[0]=int(A[0])
for i in range(1,N):
    M[i]=M[i-1]+int(A[i])
T=int(sys.stdin.readline())
for i in range(T):
    X,Y=map(int,sys.stdin.readline().split())
    if X==0:print(M[Y])
    else:print(M[Y]-M[X-1])