T=int(input())
def Z(A,B):
    k=0
    if (A=='R' and B=='S') or (A=='S' and B=='P') or (A=='P' and B=='R'):k+=1
    elif A=='R'==B or A=='S'==B or A=='P'==B:k+=0
    else:k-=1
    return k
for i in range(T):
    N=int(input())
    d=0
    for j in range(N):
        A,B=map(str,input().split())
        d+=Z(A,B)
    if d>0:print('Player 1')
    elif d==0:print('TIE')
    else:print('Player 2')