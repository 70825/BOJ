N=int(input())
for i in range(N):
    memo=[]
    num=[1,2,3,4,5,6,7,8,9]
    ans=0
    for j in range(9):
        memo.append([*map(int,input().split())])
    for j in range(9):
        if sorted(memo[j])!=num:ans+=1
    for j in range(9):
        sub_memo=[]
        for k in range(9):
            sub_memo.append(memo[k][j])
        if sorted(sub_memo)!=num:ans+=1
    for j in range(3):
        for k in range(3):
            sub_memo=[]
            for l in range(3):
                for m in range(3):
                    sub_memo.append(memo[3*j+l][3*k+m])
            if sorted(sub_memo)!=num:ans+=1
    print('Case '+str(i+1)+':',end=" ")
    if ans==0:print('CORRECT')
    else:print('INCORRECT')
    if i!=N-1:input()