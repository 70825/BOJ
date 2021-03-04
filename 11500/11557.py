T=int(input())
for i in range(T):
    N=int(input())
    X=[];Y=[]
    for j in range(N):
        A,B=input().split()
        X.append(A)
        Y.append(int(B))
    for j in range(N):
        if max(Y)==Y[j]:
            print(X[j])