memo=[['S','R'],['R','P'],['P','S']]
while 1:
    P1=str(input())
    P2=str(input())
    if P1==P2=='E':break
    w1,w2=0,0
    for i in range(len(P1)):
        if [P1[i],P2[i]] in memo:w2+=1
        elif [P2[i],P1[i]] in memo:w1+=1
    print('P1:',w1)
    print('P2:',w2)