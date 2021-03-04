T=int(input())
for i in range(T):
    S=int(input())
    N=int(input())
    for j in range(N):
        A,B=map(int,input().split())
        S+=A*B
    print(S)