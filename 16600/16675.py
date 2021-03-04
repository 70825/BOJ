M1,M2,T1,T2=map(str,input().split())
memo=[['S','R'],['R','P'],['P','S']]
if M1!=M2 and T1!=T2:print('?')
elif M1==M2 and T1!=T2:
    if [M1,T1] in memo or [M1,T2] in memo:print('TK')
    else:print('?')
elif M1!=M2 and T1==T2:
    if [T1,M1] in memo or [T1,M2] in memo:print('MS')
    else:print('?')
else:
    if [M1,T1] in memo:print('TK')
    elif [T1,M1] in memo:print('MS')
    else:print('?')