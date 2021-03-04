from decimal import *
c,b=map(Decimal,input().split())
if c%b==0:print(int(c/b))
else:print(round(c/b,9))