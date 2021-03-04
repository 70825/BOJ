a,b,c=map(int,input().split())
N=int(input())
P=[];D=[2]*(a+b+c)
for _ in range(N):
    i,j,k,r=map(int,input().split())
    if r==1:D[i-1]=D[j-1]=D[k-1]=1
    else:P.append([i,j,k])
while 1:
    k=0
    for i in range(len(P)):
        F=[];K=[]
        for j in range(len(P[i])):
            if D[P[i][j]-1]==0:F.append(P[i][j])
            elif D[P[i][j]-1]==2:K.append(P[i][j])
        if len(F)==0 and len(K)==1:D[K[0]-1]=0;k+=1
    if k==0:break
print('\n'.join(map(str,D)))