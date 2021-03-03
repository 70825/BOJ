M,N=map(int,input().split())
D=[[*input()] for _ in range(5*M+1)]
S=[0,0,0,0,0]
for i in range(M):
    for j in range(N):
        p=0
        for a in range(4):
            if D[5*i+a+1][5*j+1]=='*':p+=1
        S[p]+=1
print(' '.join(map(str,S)))