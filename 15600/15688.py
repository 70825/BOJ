import sys
T=int(input())
B=[0]*20000001
for i in range(T):N=int(sys.stdin.readline());B[N+1000000]+=1
j=0
while j!=20000001:
    if B[j]>0:print(j-1000000);B[j]-=1
    else:j+=1