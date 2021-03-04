for i in range(int(input())):
    S=input();k=''
    if len(S)>9:
        for j in range(10):k+=S[j]
        if k=='Simon says':
            for j in range(10,len(S)):print(S[j],end="")
            print("")