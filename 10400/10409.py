A,B=map(int,input().split());C=input().split();d=0;D=0
for i in range(A):
 D+=int(C[i]);d+=1
 if D>=B:break
if D>B:print(d-1)
else:print(d)