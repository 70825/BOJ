X=[];Y=[]
for i in range(3):
    A,B=map(int,input().split())
    X.append(A)
    Y.append(B)
for i in range(3):
    if X.count(X[i])==1:C=X[i]
    if Y.count(Y[i])==1:D=Y[i]
print(C,D)