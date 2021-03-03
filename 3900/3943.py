input=__import__('sys').stdin.readline
for i in range(int(input())):
    N=int(input())
    k=N
    while N!=1:
        if N%2==0:N//=2
        else:N=N*3+1
        if N>k:k=N
    print(k)