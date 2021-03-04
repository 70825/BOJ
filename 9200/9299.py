T=int(input())
for i in range(T):
    A=input().split()
    B=[]
    for j in range(1,len(A)):B.append(int(A[j])*(int(A[0])-j+1))
    print('Case '+str(i+1)+':',int(A[0])-1,end=" ")
    for j in range(len(B)-1):print(B[j],end=" ")
    print("")