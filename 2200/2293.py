def X():
    if i-j>=0:S[i]+=S[i-j]
n,k=map(int,input().split())
D,S=[],[0]*(k+1);S[0]=1
for i in range(n):
    D.append(int(input()))
for j in D:
    for i in range(1,k+1):X()
print(S[k])