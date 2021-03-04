while 1:
    A,B,C=map(int,input().split())
    if A==B==C==0:break
    k=1;D=A
    while D<C:
        D+=B
        k+=1
    if D==C:print(k)
    else:print('X')