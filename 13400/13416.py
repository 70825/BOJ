N=int(input())
for i in range(N):
 T=int(input());s=0
 for j in range(T):
  A,B,C=map(int,input().split());D=max(A,B,C)
  if D>0:s+=D
 print(s)