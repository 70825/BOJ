while 1:
    A,B=map(str,input().split())
    if A=='#' and B=='#':break
    N=int(input())
    a=0;b=0
    for i in range(N):
        C,D=map(str,input().split())
        if C==D:a+=1
        else:b+=1
    print(A,a,B,b)