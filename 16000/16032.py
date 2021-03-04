while 1:
    N=int(input())
    if N==0:break
    D=[*map(int,input().split())]
    avg=sum(D)/N
    ans=0
    for i in D:
        if i <= avg:ans+=1
    print(ans)