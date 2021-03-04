D=[]
input=__import__('sys').stdin.readline
for i in range(int(input())):
    A=input().strip().split()
    if A[0]=='push_front':D.insert(0,int(A[1]))
    elif A[0]=='push_back':D.append(int(A[1]))
    elif A[0]=='pop_front':
        if len(D)==0:print(-1)
        else:
            print(D[0])
            del D[0]
    elif A[0]=='pop_back':
        if len(D)==0:print(-1)
        else:
            print(D[len(D)-1])
            del D[len(D)-1]
    elif A[0]=='size':print(len(D))
    elif A[0]=='empty':
        if len(D)==0:print(1)
        else:print(0)
    elif A[0]=='front':
        if len(D)==0:print(-1)
        else:print(D[0])
    elif A[0]=='back':
        if len(D)==0:print(-1)
        else:print(D[len(D)-1])