import sys
while 1:
    N=int(sys.stdin.readline());D=[];s=0;k=1;a=2
    N=str(N)
    if N=='0':break
    for i in range(len(N)-1,-1,-1):
        s+=int(N[i])*k
        k*=a
        a+=1
    print(s)