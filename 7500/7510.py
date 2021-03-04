T=int(input())
for i in range(T):
 A=[0]*3;A[0],A[1],A[2]=map(int,input().split());A.sort();print("Scenario #"+str(i+1)+":")
 if A[0]**2+A[1]**2==A[2]**2:print("yes")
 else:print("no")
 print("")