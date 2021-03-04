a,b,c=map(int,input().split())
for i in range(a):
    N=int(input())
    if N<b:
        print('NTV: Dollar dropped by',b-N,'Oshloobs')
        b=N
    elif N>c:
        print('BBTV: Dollar reached',N,'Oshloobs, A record!')
        c=N;b=N
    else:b=N