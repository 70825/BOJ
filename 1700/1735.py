from fractions import Fraction
a,b=map(int,input().split())
A,B=map(int,input().split())
c=str(Fraction(a,b)+Fraction(A,B))
if c.count('/')==0:
    print(c,1)
else:
    c=c.split('/')
    print(c[0],c[1])