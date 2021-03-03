N = int(input())
for i in range(N):
    a=0;b=0;c=0;d=0
    A = int(input())
    while A > 0:
        if A>=25:
            A -= 25
            a += 1
        elif A>=10:
            A-=10
            b += 1
        elif A>=5:
            A-=5
            c +=1
        else:
            A-=1
            d+=1
    print(a,b,c,d)