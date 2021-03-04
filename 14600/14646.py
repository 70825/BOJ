import sys
n=int(input())
D=[0]*n;k=0;b=0
a=list(map(int,sys.stdin.readline().split()))
for i in range(len(a)):
    if D[a[i]-1]==0:D[a[i]-1]=1;k+=1
    else:D[a[i]-1]=0;k-=1
    if k>b:b=k
print(b)