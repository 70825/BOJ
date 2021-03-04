while 1:
    N=int(input())
    if N==0:break
    if N>=1896:
        if N>2020 and N%4==0:print(N,'No city yet chosen')
        elif 1914<=N<=1918 and N%4==0:print(N,'Games cancelled')
        elif 1939<=N<=1945 and N%4==0:print(N,'Games cancelled')
        elif N%4==0:print(N,'Summer Olympics')
        else:print(N,'No summer games')
    else:print(N,'No summer games')