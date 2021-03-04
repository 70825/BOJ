for i in range(int(input())):
    n=int(input());D=[]*n;k=0;s=0;z=0
    for j in range(n):
        a=int(input())
        k+=a;D.append(a)
        if a>z:s=j+1;z=a
    if D.count(z)>1:print('no winner')
    elif max(D)>k/2:print('majority winner',s)
    else:print('minority winner',s)