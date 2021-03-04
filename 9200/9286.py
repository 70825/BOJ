for i in range(int(input())):
    N=int(input())
    memo=[]
    for j in range(N):
        memo.append(int(input())+1)
    print('Case '+str(i+1)+':')
    for j in memo:
        if j<=6:print(j)