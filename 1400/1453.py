T=int(input())
A=input().split()
D=[];k=0
for i in range(T):
    if D.count(int(A[i]))>0:k+=1
    else:D.append(int(A[i]))
print(k)