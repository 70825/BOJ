n,k=map(int,input().split())
K=[]
Z=[]
for i in range(n):
    a,b=map(int,input().split())
    K.append(a)
    Z.append((a,b))
ans=sorted(K)[n-k]
A=[]
B=[]
for i in range(n):
    if Z[i][0]>=ans:
        A.append(Z[i][1])
        B.append((i,Z[i][1]))
A=max(A)
for i in range(n):
    if B[i][1]==A:print(B[i][0]+1);break