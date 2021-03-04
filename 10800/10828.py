input=__import__('sys').stdin.readline
T=int(input())
A=[]
for i in range(T):
    N=input().split()
    if N[0]=='push':A.insert(0,int(N[1]))
    elif N[0]=='pop':
        if len(A)==0:print('-1')
        else:print(A[0]);A.remove(A[0])
    elif N[0]=='size':print(len(A))
    elif N[0]=='empty':
        if len(A)==0:print('1')
        else:print('0')
    elif N[0]=='top':
        if len(A)==0:print('-1')
        else:print(A[0])