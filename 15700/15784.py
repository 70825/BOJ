N,a,b=map(int,input().split())
D=[[]*N]*N;k=0
for i in range(N):D[i]=list(map(int,input().split()))
for i in range(N):
    if D[i][b-1]>k:k=D[i][b-1]
if max(D[a-1])==D[a-1][b-1]==k:print('HAPPY')
else:print('ANGRY')