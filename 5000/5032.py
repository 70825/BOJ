A,B,C=map(int,input().split())
A=A+B;k=0
while A>=C:D=A//C;A=A+D-D*C;k+=D
print(k)