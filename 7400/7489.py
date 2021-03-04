for i in range(int(input())):
    k=1
    N=int(input())
    for j in range(N):
        k*=(j+1)
    k=str(k)
    for j in range(len(k)):
        if k[len(k)-1-j]!='0':
            print(k[len(k)-1-j])
            break