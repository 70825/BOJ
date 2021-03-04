def F(a,b,c,d):
    for i in range(b-1,b-1+d):
        for j in range(a-1,a-1+c):D[i][j]=S[5]
def E(a,b,c,d):
    for i in range(b-1,b-1+d):
        for j in range(a-1,a-1+c):
            if i in [b-1,b+d-2] or j in [a-1,a+c-2]:D[i][j]=S[5]
for _ in range(int(input())):
    n=int(input())
    D=[['.']*n for _ in range(n)]
    for i in range(int(input())):
        S=[*map(str,input().split())]
        a,b,c,d=int(S[1]),int(S[2]),int(S[3]),int(S[4])
        if S[0]=='Filled':F(a,b,c,d)
        else:E(a,b,c,d)
    for i in range(2):
        D=[*zip(*D[::-1])]
    for i in range(n):
        D[i]=D[i][::-1]
    print('Case',str(_+1)+':')
    for i in range(n):
        print(''.join(D[i]))