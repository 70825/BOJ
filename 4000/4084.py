while 1:
    A,B,C,D=map(int,input().split());k=0
    if A==B==C==D==0:break
    while A!=B or B!=C or C!=D:a=abs(A-B);b=abs(B-C);c=abs(C-D);d=abs(D-A);A=a;B=b;C=c;D=d;k+=1
    print(k)