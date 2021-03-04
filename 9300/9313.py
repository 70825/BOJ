while 1:
    N=int(input())
    if N==-1:break
    M=bin(N)[2::]
    M=('0'*(32-len(M))+M)[::-1]
    print(int(M,2))