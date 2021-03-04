n,m=map(int,input().split())
def check(G):
    for i in range(len(G)):
        k=''.join(G[i])
        if 'SW' in k or 'WS' in k:print(0);exit()
D=[[*input()] for _ in range(n)]
S=[*zip(*D[::-1])]
check(D);check(S)
for i in range(n):
    for j in range(m):
        if D[i][j]=='.':D[i][j]='D'
print(1)
for i in range(n):print(''.join(D[i]))