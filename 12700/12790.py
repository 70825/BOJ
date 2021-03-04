T=int(input())
for i in range(T):
 a,b,c,d,A,B,C,D=map(int,input().split())
 A=a+A;B=b+B;C=C+c;D=D+d
 if A<1:A=1
 if B<1:B=1
 if C<0:C=0
 print(A+5*B+2*C+2*D)