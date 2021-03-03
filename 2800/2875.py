N,M,K = map(int,input().split())
T = 0
while 1:
    if N>=2 and M>=1:
        N-=2
        M-=1
        T+=1
    else:
        break
if N+M >= K:
    print(T)
else:
    K -= N+M
    if K <= 3:
        T -= 1
    elif K > 3:
        if K % 3 == 0:
            T -= K //3
        else:
            T -= K//3+1
    print(T)