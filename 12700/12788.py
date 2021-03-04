N=int(input())
M,K=map(int,input().split())
A=sorted([*map(int,input().split())],reverse=True)
ans=0;t=0
for i in range(N):
    ans+=A[i];t+=1
    if ans>=M*K:break
print(['STRESS',t][ans>=M*K])