n=int(input())
import sys
a=[[]*n for i in range(n)];s=0
for i in range(n):a[i]=list(map(int,sys.stdin.readline().split()))
for i in range(n):s+=sum(a[i])
print(s)