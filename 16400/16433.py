N,R,C=map(int,input().split())
D=[['.']*N for _ in range(N)]
a,b=R%2,C%2
for i in range(N):
    for j in range(N):
        if i%2==a and j%2==b:D[i][j]='v'
        if i%2!=a and j%2!=b:D[i][j]='v'
for i in range(N):
    print(''.join(map(str,D[i])))