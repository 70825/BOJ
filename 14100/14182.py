while 1:
    N=int(input())
    if N==0:break
    if N<=1000000:print(N)
    elif N<=5000000:print(int(N*0.9))
    else:print(int(N*0.8))