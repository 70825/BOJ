for i in range(int(input())):
    g=0
    for j in range(int(input())):
        A=str(input())
        if A=='000' or A=='001' or A=='100':g+=1
    print('Case '+str(i+1)+':',end=" ")
    if g==0:print('Standing')
    else:print('Fallen')