A,B=map(int,input().split())
C,D=map(int,input().split())
while B>0 and D>0:B-=C;D-=A
if D<=0 and B<=0:print('DRAW')
elif B<=0:print('PLAYER B')
else:print('PLAYER A')