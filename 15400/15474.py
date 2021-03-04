A,B,C,D,E=map(int,input().split())
a=0;m=0
b=0;n=0
while a<A:
    a+=B
    m+=C
while b<A:
    b+=D
    n+=E
print(min(m,n))