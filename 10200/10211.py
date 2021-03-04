for _ in range(int(input())):
    n=int(input())
    D=[*map(int,input().split())]
    for i in range(1,n):
        D[i]=max(D[i-1]+D[i],D[i])
    print(max(D))