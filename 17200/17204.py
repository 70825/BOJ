N,K=map(int,input().split())
D=[int(input()) for i in range(N)]
S=[1]+[0]*(N-1)
ans=0
go=0
for i in range(N):
    if go==K: print(ans);break
    elif S[D[go]]==0:ans+=1;S[D[go]]=1;go=D[go]
    else:print(-1);break