while 1:
    A=int(input())
    if A==0:break
    for i in range(A):
        for j in range(i+1):
            print('*',end="")
        print("")