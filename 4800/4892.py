k=1
while 1:
    N=int(input())
    if N==0:
        break
    else:
        a=3*N
        if a%2==0:
            print(str(k)+".","even",end=" ")
            b=a//2
        else:
            print(str(k)+".","odd",end=" ")
            b=(a+1)//2
        c=3*b
        d=c//9
        print(d)
        k+=1