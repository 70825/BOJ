n,k=map(int,input().split())
D=[int(input()) for _ in range(n)]
S=[-1]*(k+1);S[0]=0
for i in D:
    for j in range(k+1):
        if j-i>=0 and S[j-i]!=-1:
            if S[j]==-1:S[j]=S[j-i]+1
            else:S[j]=min(S[j],S[j-i]+1)
print(S[k])