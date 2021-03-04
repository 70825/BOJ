T=int(input())
A=[[0]*2 for i in range(T)];B=[];C=[]
for i in range(T):
    x,y=map(int,input().split())
    A[i][0]=x;C.append(x)
    A[i][1]=y
A.sort(reverse=True)
for i in range(5):
    B.append(A[0][0])
    C.remove(A[0][0])
    del A[0]
print(C.count(B[4]))