while 1:
    D=[*map(int,input().split())]
    if max(D)==0:break
    k=(sum(D)-min(D)-max(D))/4
    if k==int(k):print(int(k))
    else:print(k)