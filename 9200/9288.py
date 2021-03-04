for i in range(int(input())):
    N=int(input())
    print('Case '+str(i+1)+':')
    for j in range(N//2):
        A=j+1;B=N-A
        if 1<=A<=6 and 1<=B<=6:print('('+str(A)+','+str(B)+')')