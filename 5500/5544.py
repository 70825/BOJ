N=int(input())
A=[0]*N;k=1;C=[0]*N
for i in range(N*(N-1)//2):
    a,b,c,d=map(int,input().split())
    if c>d:A[a-1]+=3
    elif c==d:A[a-1]+=1;A[b-1]+=1
    else:A[b-1]+=3
B=list(set(A))
B.sort(reverse=True)
for i in range(len(B)):
    for j in range(len(A)):
        if B[i]==A[j]:C[j]=k
    m=A.count(B[i])
    k+=m
for i in range(N):
    print(C[i])