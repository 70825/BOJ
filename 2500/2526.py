n,p=map(int,input().split())
D=[n];k=n
while 1:
    a=(k*n)%p
    if a in D:
        for i in range(len(D)):
            if D[i] == a:
                print(len(D)-i)
                exit()
    D.append(a);k=a