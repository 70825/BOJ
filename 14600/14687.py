N=int(input())
D=sorted([*map(int,input().split())])
if N%2==1:print(D[N//2],end=" ");del D[N//2]
A=sorted(D[:N//2:],reverse=True)
B=sorted(D[N//2:])
if N%2==1:
    for i in range(N//2):
        print(B[i],A[i],end=" ")    
else:
    for i in range(N//2):
        print(A[i],B[i],end=" ")