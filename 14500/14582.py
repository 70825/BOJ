A=[0]*9;B=[0]*9;k=0;a=0;b=0
A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8]=map(int,input().split())
B[0],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8]=map(int,input().split())
for i in range(18):
    if i%2==0:a+=A[i//2]
    else:b+=B[i//2]
    if b>=a:k+=1
if k==18:print('No')
else:print('Yes')