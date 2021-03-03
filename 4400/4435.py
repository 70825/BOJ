for i in range(int(input())):
    G=[*map(int,input().split())]
    E=[*map(int,input().split())]
    g=1*G[0]+2*G[1]+3*G[2]+3*G[3]+4*G[4]+10*G[5]
    e=1*E[0]+2*E[1]+2*E[2]+2*E[3]+3*E[4]+5*E[5]+10*E[6]
    print('Battle '+str(i+1)+':',end=" ")
    if g>e:print('Good triumphs over Evil')
    elif e>g:print('Evil eradicates all trace of Good')
    else:print('No victor on this battle field')