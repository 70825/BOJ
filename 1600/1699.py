N=int(input())
S=[0]*(N+1)
for i in range(1,N+1):
    S[i]=i;j=1
    while j*j<=i:S[i]=min(S[i],S[i-j*j]+1);j+=1
print(S[N])