N=int(input())
D=[*map(int,input().split())]
p=0
for i in range(2,N):
    if N%i==0:p=1;break
if p==0:print('Yes')
else:print('No')