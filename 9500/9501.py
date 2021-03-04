for i in range(int(input())):
 N,D=map(int,input().split());k=0
 for j in range(N):
  A,B,C=map(int,input().split())
  if A*B/C>=D:k+=1
 print(k)