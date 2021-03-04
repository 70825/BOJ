def go(x,y,t):
    if t=='U' and 0<=x-1 and Map[x-1][y]!='#':return x-1,y
    if t=='D' and x+1<n and Map[x+1][y]!='#':return x+1,y
    if t=='L' and 0<=y-1 and Map[x][y-1]!='#':return x,y-1
    if t=='R' and y+1<m and Map[x][y+1]!='#': return x,y+1
    return x,y
def Status(name=None):
    if killed_by_monster==0 and killed_by_trap==0:Map[x][y]='@'
    for i in range(n):
        print(''.join(map(str,Map[i])))
    print('Passed Turns : {}'.format(turn+1))
    print('LV : {}'.format(Player['LV']))
    print('HP : {}/{}'.format(Player['now_HP'],Player['max_HP']))
    print('ATT : {}+{}'.format(Player['ATK'],Ring['W']))
    print('DEF : {}+{}'.format(Player['DEF'],Ring['A']))
    print('EXP : {}/{}'.format(Player['now_EXP'],Player['max_EXP']))
    if kill_boss:
        print('YOU WIN!')
    elif killed_by_monster:print('YOU HAVE BEEN KILLED BY {}..'.format(name))
    elif killed_by_trap:print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
    else:
        print('Press any key to continue.')
    exit(0)
def Reincarnation():
    global x,y,turn
    Ring['RE']=0
    Ring['have']-=1
    Player['now_HP']=Player['max_HP']
    x,y=start
def Trap():
    global killed_by_trap
    if Ring['DX']==1:Player['now_HP']-=1
    else:Player['now_HP']-=5
    if Player['now_HP']<=0:
        if Ring['RE']==1:Reincarnation()
        else:
            killed_by_trap=1
            Status()
def Chest():
    Map[x][y] = '.'
    t=Num_info[x][y]
    T,S=Chest_info[t]
    if T in 'WA':Ring[T]=S
    if T=='O' and Ring[S]==0 and Ring['have']<4:
        Ring[S]=1;Ring['have']+=1
def Attack():
    global killed_by_monster,kill_boss
    t=Num_info[x][y]
    S,W,A,H,E=Mon_info[t]
    now_H=H
    ATT=Player['ATK']+Ring['W']
    DEF=Player['DEF']+Ring['A']
    time=0
    if Ring['HU']==1 and Map[x][y]=='M':Player['now_HP']=Player['max_HP']
    while Player['now_HP']>0:
        if time==0 and Ring['CO']==1:
            if Ring['DX']==1:now_H-=max(1,ATT*3-A)
            else:now_H-=max(1,ATT*2-A)
        else:now_H-=max(1,ATT-A)
        if now_H<=0:break
        if Map[x][y]=='M' and Ring['HU']==1 and time==0:Player['now_HP']-=0
        else:Player['now_HP']-=max(1,W-DEF)
        time+=1
    if Player['now_HP']<=0:
        if Ring['RE']==1:Reincarnation()
        else:
            killed_by_monster=1
            Player['now_HP']=0
            Status(S)
    else:
        EXP=E
        if Ring['EX']==1:EXP=int(EXP*1.2)
        if Ring['HR']==1:Player['now_HP']=min(Player['max_HP'],Player['now_HP']+3)
        Player['now_EXP']+=EXP
        if Player['max_EXP']<=Player['now_EXP']:
            Player['LV']+=1
            Player['max_HP']+=5
            Player['now_HP']=Player['max_HP']
            Player['max_EXP']=5*Player['LV']
            Player['now_EXP']=0
            Player['ATK']+=2
            Player['DEF']+=2
        if Map[x][y]=='M':
            Map[x][y]='@'
            kill_boss=1
            Status()
        else:Map[x][y]='.'
n,m=map(int,input().split())
dx,dy=[1,-1,0,0],[0,0,1,-1]
Map=[[*input()] for _ in range(n)]
Num_info=[[-1]*m for _ in range(n)]
Mon_info=[]
Chest_info=[]
Player={'LV':1, 'now_HP':20, 'max_HP':20, 'ATK':2, 'DEF':2, 'now_EXP':0, 'max_EXP':5}
Ring={'have':0, 'W':0, 'A':0, 'HR':0, 'RE':0, 'CO':0, 'EX':0, 'DX':0, 'HU': 0, 'CU': 0}
Move=[*input()]
k=0;L=0
start=[0,0]
for i in range(n):
    for j in range(m):
        if Map[i][j] in '&M':k+=1
        if Map[i][j]=='B':L+=1
        if Map[i][j]=='@':start=[i,j];Map[i][j]='.'
for i in range(k):
    R,C,S,W,A,H,E=input().split()
    R=int(R)-1;C=int(C)-1;W=int(W);A=int(A);H=int(H);E=int(E)
    Num_info[R][C]=i
    Mon_info.append([S,W,A,H,E])
for i in range(L):
    R,C,T,S=input().split()
    R=int(R)-1;C=int(C)-1
    Num_info[R][C]=i
    if T in 'WA':Chest_info.append([T,int(S)])
    else:Chest_info.append([T,S])
turn=0
kill_boss=0
killed_by_monster=0
killed_by_trap=0
x,y=start
while 1:
    x,y=go(x,y,Move[turn])
    if Map[x][y]=='^':Trap()
    if Map[x][y]=='B':Chest()
    if Map[x][y] in '&M':Attack()
    if turn==len(Move)-1:Status()
    turn+=1