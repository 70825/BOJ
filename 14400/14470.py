A=[0]*5;k=0
for i in range(5):
    A[i]=int(input())
while A[0]!=A[1]:
    if A[0]<0:k+=A[2]
    elif A[0]==0:k+=A[3]+A[4]
    else:k+=A[4]
    A[0]+=1
print(k)