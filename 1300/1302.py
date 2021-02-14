A={}
for i in range(int(input())):
    S=input()
    if S in A:A[S]+=1
    else:A[S]=1
B=max(A.values())
C=list(A.keys())
C.sort()
for i in range(len(C)):
    if A[C[i]]==B:print(C[i]);break