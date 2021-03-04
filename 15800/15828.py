import sys
N=int(input())
Router=[]*N
while 1:
    a=int(sys.stdin.readline())
    if a==-1:break
    if a!=0:
        if len(Router)<N:
            Router.append(a)
    else:
        Router.pop(0)
if len(Router)==0:
    print('empty')
else:
    for i in Router:
        print(i,end=" ")