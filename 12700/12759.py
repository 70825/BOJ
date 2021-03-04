N=[['0']*3 for i in range(3)];A=int(input());k=0
if A==1:B=2
else:B=1
def tic(N):
    D=[]
    for i in range(3):
        D.append(N[i][0]+N[i][1]+N[i][2])
        D.append(N[0][i]+N[1][i]+N[2][i])
    D.append(N[0][0]+N[1][1]+N[2][2])
    D.append(N[0][2]+N[1][1]+N[2][0])
    return D
for i in range(9):
    x,y=map(int,input().split())
    x-=1;y-=1
    if A==1:
        if i%2==0:N[x][y]='1'
        else:N[x][y]='2'
    else:
        if i%2==0:N[y][x]='2'
        else:N[y][x]='1'
    if k==0:
        if '111' in tic(N):k=1
        elif '222' in tic(N):k=2
if k!=0:print(k)
else:print(0)