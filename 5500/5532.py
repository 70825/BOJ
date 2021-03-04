L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
x=0;y=0;
x+=A//C
if A%C>0:x+=1
y+=B//D
if B%D>0:y+=1
print(L-max(x,y))