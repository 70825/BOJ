while 1:
 try:
  A,B=map(int,input().split())
  if A==0==B:break
  print(A*2-B)
 except EOFError:break