for i in range(int(input())):
    a,b=map(int,input().split())
    print('Scenario #'+str(i+1)+':')
    print(b*(b+1)//2-(a-1)*a//2)
    print("")