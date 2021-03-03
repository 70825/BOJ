while 1:
    A,B,C=map(str,input().split())
    if A=='#' and B=='0' and C=='0':break
    B=int(B);C=int(C)
    print(A,end=" ")
    if B>17 or C>=80:print('Senior')
    else:print('Junior')