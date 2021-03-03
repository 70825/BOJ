while 1:
    try:
        D=[*map(int,input().split())]
        x=D.pop(0);check=[0]*(x)
        for i in range(1,x):
            k=abs(D[i]-D[i-1])
            if k!=0 and k<x:check[abs(D[i]-D[i-1])]=1
        print('Jolly' if sum(check)==x-1 else 'Not jolly')
    except EOFError:break