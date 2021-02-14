input=__import__('sys').stdin.readline
for i in range(3):
    N=int(input())
    k=0
    for j in range(N):
        k+=int(input())
    if k>0:print('+')
    elif k==0:print(0)
    else:print('-')