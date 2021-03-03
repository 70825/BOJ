x=[]
for _ in range(int(input())):
    D=[*map(int,input().split())]
    z=D.pop(0)
    avg=sum(D)/z
    t=0
    for i in range(z):
        if D[i]>avg:t+=1
    x.append(t/z*100)
for _ in range(len(x)):
    print('{:.3f}%'.format(x[_]))