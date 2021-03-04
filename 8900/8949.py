A,B=map(str,input().split())
D=[0]*max(len(A),len(B))
for i in range(len(D)):
    if len(A)>=i+1:D[len(D)-1-i]+=int(A[len(A)-1-i])
    if len(B)>=i+1:D[len(D)-1-i]+=int(B[len(B)-1-i])
for i in range(len(D)):print(D[i],end="")