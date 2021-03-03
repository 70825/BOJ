while 1:
    N=int(input())
    if N==0:break
    memo=str(input())
    sub_memo=[]
    for i in range(0,len(memo),N):
        sub_memo.append(memo[i:i+N])
    message=''
    for i in range(N):
        for j in range(len(sub_memo)):
            if j%2==0:
                message+=sub_memo[j][i]
            else:
                message+=sub_memo[j][N-1-i]
    print(message)