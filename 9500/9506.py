while 1:
    N=int(input())
    if N==-1:break
    memo=[]
    for i in range(1,N):
        if N%i==0:memo.append(i)
    if sum(memo)==N:
        print(N,'=',end=" ")
        print(' + '.join(map(str,memo)))
    else:print(N,'is NOT perfect.')