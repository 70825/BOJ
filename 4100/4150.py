N=int(input())
B=[1,0];d=1
if N==1:
    print(1)
else:
    k=0
    while d!=N:
        k=B[0]+B[1]
        B[1]=B[0]
        B[0]=k
        d+=1
    print(k)