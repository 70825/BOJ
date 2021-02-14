import sys
D=[10,1,2,3,4,5,6,7,8,9]
for i in range(int(input())):
    m,n=map(int,sys.stdin.readline().split())
    if n%4==0:print(D[m**4%10])
    else:print(D[m**(n%4)%10])