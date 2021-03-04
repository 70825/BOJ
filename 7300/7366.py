for i in range(int(input())):
    N=int(input())
    D=[*map(str,input().split())]
    print('Case '+str(i+1)+':','This list contains',D.count('sheep'),'sheep.')
    print("")