N = int(input())
C = 0
if 1<= N <= 2100000000:
    for i in range(0,int(N**(1/2))):
        if (i+1)**2<=N<(i+2)**2:
            C = i+1
if C != 0:
    print(C)