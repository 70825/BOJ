def Check():
    ans=0
    for i in range(5):
        if ''.join(map(str,K[i]))=='OOOOO':ans+=1
    for j in range(5):
        if K[0][j]+K[1][j]+K[2][j]+K[3][j]+K[4][j]=='OOOOO':ans+=1
    if K[0][0]+K[1][1]+K[2][2]+K[3][3]+K[4][4]=='OOOOO':ans+=1
    if K[0][4]+K[1][3]+K[2][2]+K[3][1]+K[4][0]=='OOOOO':ans+=1
    if ans>=3:print(t+1);exit()
D=[[*map(int,input().split())] for _ in range(5)]
K=[['.']*5 for _ in range(5)]
S=[[*map(int,input().split())] for _ in range(5)]
for t in range(25):
    a=t//5
    b=t%5
    for i in range(5):
        for j in range(5):
            if D[i][j]==S[a][b]:
                K[i][j]='O';Check()