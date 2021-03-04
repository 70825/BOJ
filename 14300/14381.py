T=int(input())
for i in range(T):
    A = int(input());d=1;D=[0,0,0,0,0,0,0,0,0,0]
    print('Case #'+str(i+1)+':',end=" ")
    while d!=200:
        K=str(d*A)
        for j in range(len(K)):
            D[int(K[j])]+=1
        if min(D)>0:print(d*A);break
        d+=1
        if d==200:print('INSOMNIA')