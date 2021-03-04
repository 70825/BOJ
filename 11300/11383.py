N,M=map(int,input().split())
D=['']*N;d=['']*N;k=0
for i in range(N):D[i]=str(input())
for i in range(N):
    for j in range(len(D[i])):d[i]+=D[i][j]*2
for i in range(N):
    S=str(input())
    if d[i]==S:k+=1
if k==N:print('Eyfa')
else:print('Not Eyfa')