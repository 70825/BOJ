A=str(input())
T=int(input())
D=[]
for i in range(len(A)):D.append(A[i])
for i in range(T):
    M,N=map(int,input().split());t=D[M];D[M]=D[N];D[N]=t
for i in range(len(D)):print(D[i],end="")