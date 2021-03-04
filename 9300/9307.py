while 1:
    A=[*map(float,input().split())]
    if A[0]==-1:break
    s=int(A.pop(3))
    k=3
    print('Month ' + str(s) + ' cost: $', end="")
    while 1:
        if s-1<=2:
            a=int(A[s-1]);b='{:.2f}'.format(A[s-1]%1)
            print('{:,}'.format((a))+str(b)[1::]);break
        else:
            A.append(round(A[k-3]*A[k-2]/A[k-1],2))
            if s-1==k:
                a=int(A[k]);b='{:.2f}'.format(A[k]%1)
                print('{:,}'.format(a)+str(b)[1::]);break
            else:k+=1