k=1
while 1:
    N=int(input())
    if N==0:break
    memo=[]
    for i in range(N):
        D=[*map(str,input().split())]
        memo.append(D)
    nasty=0
    if k!=1:print('')
    print('Group',k)
    for i in range(N):
        for j in range(1,N):
            if memo[i][j]=='N':
                ans=i-j
                if ans<0:ans+=N
                print(memo[ans][0],'was nasty about',memo[i][0])
                nasty+=1
    if nasty==0:
        print('Nobody was nasty')
    k+=1