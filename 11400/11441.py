import sys
int(input())
A=list(map(int,sys.stdin.readline().split()))
A.insert(0,0)
for i in range(1,len(A)):A[i]+=A[i-1]
for i in range(int(input())):
    x,y=map(int,sys.stdin.readline().split())
    print(A[y]-A[x-1])