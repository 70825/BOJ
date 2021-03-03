for i in range(int(input())):
    N=int(input())
    N_memo=[]
    N_sub_memo=[0]*N
    for j in range(N):
        N_memo.append(input())
    M=int(input())
    M_memo=[]
    for j in range(M):
        M_memo+=[*map(str,input().split())]
    for j in range(N):
        if N_memo[j] in M_memo:N_sub_memo[j]=1
    if i!=0:print('')
    print('Test set '+str(i+1)+':')
    for j in range(N):
        print(N_memo[j],'is',end=" ")
        if N_sub_memo[j]==1:print('present')
        else:print('absent')