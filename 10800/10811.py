N,M=map(int,input().split());A=[0]*N
for i in range(N):A[i]=i+1
for i in range(M):
 B,C=map(int,input().split());D=[]
 for j in range(B-1,C):D.append(A[j])
 for j in range(len(D)):A[j+B-1]=D[len(D)-1-j]
for i in range(N):print(A[i],end=" ")