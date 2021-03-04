A=str(input());k=0
for i in range(len(A)):
    if A[i]=='x':k=i;break
if A[0]!='x' and k==0:print(0)
elif A[0]=='x' and k==0:
    print(1)
elif k==1 and A[0]=='-':
    print(-1)
else:
    for i in range(k):
        print(A[i],end="")