import sys
T=int(input())
for i in range(T):
    A,B=map(int,sys.stdin.readline().split());a=0;b=0
    if A==B:
        print(A,a)
    else:
        while a+b!=B:
            A-=2;a+=1;b=A
        print(b,a)