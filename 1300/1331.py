S=[[0]*6 for _ in range(6)]
A=input()
a,b=ord(A[0])-65,int(A[1])-1
m,n=a,b
S[a][b]=1
dx,dy=[2,2,1,1,-1,-1,-2,-2],[1,-1,2,-2,2,-2,1,-1]
for i in range(35):
    B=input()
    c,d=ord(B[0])-65,int(B[1])-1
    z=0
    for j in range(8):
        nx,ny=m+dx[j],n+dy[j]
        if c==nx and d==ny:z+=1;m=nx;n=ny
    if S[m][n]==0 and z==1:S[m][n]=1;continue
    else:print('Invalid');exit()
for i in range(8):
    nx,ny=m+dx[i],n+dy[i]
    if nx==a and ny==b:print('Valid');exit()
print('Invalid')