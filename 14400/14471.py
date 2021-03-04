N,M=map(int,input().split());C=[0]*M;d=0;m=0
for i in range(M):
    A,B=map(int,input().split());C[i]=N-A
    if A>=N:C[i]=0;m+=1
    if C[i]<=0:C[i]=0
    d+=C[i]
for i in range(M):
    if max(C)==C[i]:d-=C[i]
print(d)