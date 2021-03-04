k=1
while 1:
    A,B=map(str,input().split())
    if A=='#' and B=='#':break
    N=int(input());C=['a']*N
    for i in range(N):
        C[i]=str(input())
        C[i]=C[i].replace(A.lower(),'_')
        C[i]=C[i].replace(A.upper(),'_')
        C[i]=C[i].replace(B.lower(),'_')
        C[i]=C[i].replace(B.upper(),'_')
    print('Case',k)
    for i in range(len(C)):print(C[i])
    k+=1
    print("")