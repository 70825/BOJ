input()
D=[*map(int,input().split())]
for i in range(len(D)):
    k=0
    for j in range(1,D[i]):
        if D[i]%j==0:k+=j
    if k<D[i]:print('Deficient')
    elif k==D[i]:print('Perfect')
    else:print('Abundant')