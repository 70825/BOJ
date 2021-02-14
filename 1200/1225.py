A,B=map(str,input().split())
a=[]
b=[]
for i in range(len(A)):
    a.append(int(A[i]))
for i in range(len(B)):
    b.append(int(B[i]))
print(sum(a)*sum(b))