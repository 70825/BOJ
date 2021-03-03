while 1:
    A=[0]*3
    A[0],A[1],A[2]=map(int,input().split())
    if min(A)==0 and max(A)==0:break
    A.sort()
    if A[2]**2==A[1]**2+A[0]**2:print('right')
    else:print('wrong')