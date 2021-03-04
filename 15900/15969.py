import sys
T=int(input())
A=sys.stdin.readline().split()
D=[]
for i in range(T):D.append(int(A[i]))
print(max(D)-min(D))