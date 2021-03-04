T=int(input())
for i in range(T):
    N=int(input())
    d=0
    while 1:
        if d+d**2<=N:d+=1
        else: d-=1;break
    print(d)