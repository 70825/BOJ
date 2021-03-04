while 1:
    D=[*map(int,input().split())]
    if len(D)==1:break
    memo=[]
    for i in range(0,D[0]//2,2):
        memo.append([i+1,i+2,D[0]-1-i,D[0]-i])
    for i in memo:
        if D[1] in i:
            for j in i:
                if D[1]!=j:print(j,end=" ")
    print("")