A=str(input())
D=[];s=0;k=0
for i in range(len(A)):
    if A[i]=='(':D.insert(0,A[i]);k+=1
    elif A[i]==')' and A[i-1]=='(':k-=1;s+=k;del D[0]
    elif A[i]==')' and A[i-1]==')':k-=1;s+=1
print(s)