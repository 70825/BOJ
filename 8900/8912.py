for i in range(int(input())):
    N=int(input())
    ans=0
    D=[*map(int,input().split())]
    for j in range(1,N):
        for k in range(j):
            if D[j]>=D[k]:ans+=1
    print(ans)