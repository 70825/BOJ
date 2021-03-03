A={};B={}
import sys
input=lambda:sys.stdin.readline().strip()
n,m=map(int,input().split())
for i in range(1,n+1):
    k=input()
    A[k]=i;B[i]=k
for i in range(m):
    p=input()
    if 48<=ord(p[0])<=57:print(B[int(p)])
    else:print(A[p])