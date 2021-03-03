N=int(input())
while 1:
 A=int(input())
 if A==0:break
 if A%N==0:print(A,'is a multiple of',str(N)+'.')
 else:print(A,'is NOT a multiple of',str(N)+'.')