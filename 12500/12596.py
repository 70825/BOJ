for i in range(int(input())):
    N=int(input())
    memo=[*map(int,input().split())]
    print('Case #'+str(i+1)+':',end=" ")
    for j in memo:
        if memo.count(j)==1:print(j);break