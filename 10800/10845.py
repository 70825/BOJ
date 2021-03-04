input=__import__('sys').stdin.readline
T=int(input())
D=[]
for i in range(T):
    A=input().strip().split()
    if A[0]=='push':
        D.append(int(A[1]))
    elif A[0]=='pop':
        if len(D)==0:print(-1)
        else:print(D[0]);del D[0]
    elif A[0]=='size':
        print(len(D))
    elif A[0]=='empty':
        if len(D)==0:print(1)
        else:print(0)
    elif A[0]=='front':
        if len(D)==0:print(-1)
        else:print(D[0])
    elif A[0]=='back':
        if len(D)==0:print(-1)
        else:print(D[len(D)-1])