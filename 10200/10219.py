for _ in range(int(input())):
    n,m=map(int,input().split())
    D=[input() for i in range(n)]
    print('\n'.join(D[::-1]))