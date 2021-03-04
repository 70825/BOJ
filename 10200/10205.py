for i in range(int(input())):
    h=int(input())
    S=input()
    for j in range(len(S)):
        if S[j]=='c':h+=1
        else:h-=1
    print('Data Set '+str(i+1)+':')
    print(h)
    print("")