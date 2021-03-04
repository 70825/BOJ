n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
for i in range(m):
    for j in range(n-1,-1,-1):
        if D[j][i]=='o':
            for k in range(j+1,n):
                if D[k][i] in '#o':break
                if D[k][i]=='.':D[k][i]='o';D[k-1][i]='.'
for i in range(n):
    print(''.join(D[i]))