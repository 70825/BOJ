for i in range(int(input())):
    N=input()
    k=str(int(N)**2)
    if k[len(k)-len(N)::]==N:print('YES')
    else:print('NO')