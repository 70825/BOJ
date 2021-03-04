N,M=map(int,input().split());D=[0]*N
for i in range(N):D[i]=i+1
for i in range(M):a,b=map(int,input().split());k=D[a-1];D[a-1]=D[b-1];D[b-1]=k
for i in range(N):print(D[i],end=" ")