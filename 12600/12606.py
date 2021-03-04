for i in range(int(input())):
    A=[*map(str,input().split())]
    print('Case #'+str(i+1)+':',' '.join(map(str,A[::-1])))