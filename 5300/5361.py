import sys
N = int(input())
for i in range(N):
    A,B,C,D,E = map(int,sys.stdin.readline().split())
    S = (A*350.34)+(B*230.90)+(C*190.55)+(D*125.30)+(E*180.90)
    print("$",end="")
    print("{:.2f}".format(S))