for i in range(int(input())):
    J,N=map(int,input().split())
    memo=[]
    for j in range(N):
        R,C=map(int,input().split())
        memo.append(R*C)
    ans,k=0,0
    for j in sorted(memo,reverse=True):
        ans+=j;k+=1
        if ans>=J:break
    print(k)