A=[*map(int,input().split())]
B=[*map(int,input().split())]
ans=0
for i in range(5):
    if A[i]==1 and B[i]==0:ans+=1
    elif A[i]==0 and B[i]==1:ans+=1
if ans==5:print('Y')
else:print('N')