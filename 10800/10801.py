A=input().split();B=input().split();a=0;b=0
for i in range(10):
 if int(A[i])>int(B[i]):a+=1
 elif int(A[i])<int(B[i]):b+=1
if a==b:print("D")
elif a>b:print("A")
else:print("B")