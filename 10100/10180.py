for i in range(int(input())):
    N,D=map(int,input().split())
    ans=0
    for j in range(N):
        vi,fi,ci=map(int,input().split())
        if vi*fi/ci>=D:ans+=1
    print(ans)