A=[1,0,0]
B=str(input())
for i in range(len(B)):
    if B[i]=='A':k=A[0];A[0]=A[1];A[1]=k
    elif B[i]=='B':k=A[1];A[1]=A[2];A[2]=k
    else:k=A[2];A[2]=A[0];A[0]=k
for i in range(3):
    if A[i]==1:print(i+1)