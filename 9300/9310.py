while 1:
    N=int(input())
    if N==0:break
    D=[*map(int,input().split())]
    if D[0]==D[1]:print(D[0]*N)
    elif D[1]/D[0]==D[2]/D[1]:
        k=D[1]//D[0]
        print(D[0]*(k**N-1)//(k-1))
    else:
        k=D[1]-D[0]
        print(N*(2*D[0]+(N-1)*k)//2)