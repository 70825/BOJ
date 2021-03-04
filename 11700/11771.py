N=int(input())
D=[];err=0;x=0
S=[['*']*N for _ in range(N)]
for i in range(N):D.append(input())
message=input()
for i in range(4):
    for j in range(N):
        for k in range(N):
            if D[j][k]=='.':
                if S[j][k]=='*':S[j][k]=message[x];x+=1
                else:err+=1
    D=[*zip(*D[::-1])]
for i in range(N):
    for j in range(N):
        if S[i][j]=='*':err+=1
if err==0:
    for i in range(N):
        print(''.join(map(str,S[i])),end='')
else:print('invalid grille')