for i in range(int(input())):
    A=[0,0,0]
    A[0],A[1],A[2]=map(int,input().split())
    A.sort()
    print('Case #'+str(i+1)+':',end=" ")
    if A[0]==A[1]==A[2]:print('equilateral')
    elif (A[0]==A[1] and A[0]*2>A[2]) or (A[1]==A[2] and A[1]*2>A[0]):print('isosceles')
    elif A[0]+A[1]>A[2]:print('scalene')
    else:print('invalid!')