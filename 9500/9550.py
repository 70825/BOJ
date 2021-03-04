T=int(input())
for i in range(T):
 d=0;A,B=map(int,input().split());C=input().split()
 for j in range(A):
  if int(C[j])//B>0:d+=int(C[j])//B
 print(d)