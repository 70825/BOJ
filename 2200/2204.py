while 1:
    N=int(input())
    if N==0:break
    memo=[]
    sub_memo=[]
    for i in range(N):
        A=str(input())
        sub_memo.append(A.lower())
        memo.append(A)
    sub_memo.sort()
    for i in range(N):
        if sub_memo[0]==memo[i].lower():
            print(memo[i])
            break