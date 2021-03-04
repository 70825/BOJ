while 1:
    A,B=map(int,input().split())
    if A==B==0:break
    print(min(A*30+B*40,A*35+B*30,A*40+B*20))