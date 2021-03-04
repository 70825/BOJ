for i in range(int(input())):
    memo=[]
    for j in range(3):
        S=str(input())
        memo.append([S[0],S[1],S[2]])
    S=str(input())
    D=['xx-','x-x','-xx']
    E=['oo-','o-o','-oo']
    ans=0
    if S=='x':
        for j in range(3):
            if memo[j][0]+memo[j][1]+memo[j][2] in D:
                if memo[j][0]=='-':memo[j][0]='x'
                elif memo[j][1]=='-':memo[j][1]='x'
                else:memo[j][2]='x'
                ans=1
            if ans==0 and memo[0][j]+memo[1][j]+memo[2][j] in D:
                if memo[0][j]=='-':memo[0][j]='x'
                elif memo[1][j]=='-':memo[1][j]='x'
                else:memo[2][j]='x'
                ans=1
        if ans==0 and memo[0][0]+memo[1][1]+memo[2][2] in D:
            if memo[0][0]=='-':memo[0][0]='x'
            elif memo[1][1]=='-':memo[1][1]='x'
            else:memo[2][2]='x'
            ans=1
        if ans==0 and memo[0][2]+memo[1][1]+memo[2][0] in D:
            if memo[0][2]=='-':memo[0][2]='x'
            elif memo[1][1]=='-':memo[1][1]='x'
            else:memo[2][0]='x'
    if S=='o':
        for j in range(3):
            if memo[j][0]+memo[j][1]+memo[j][2] in E:
                if memo[j][0]=='-':memo[j][0]='o'
                elif memo[j][1]=='-':memo[j][1]='o'
                else:memo[j][2]='o'
                ans=1
            if ans==0 and memo[0][j]+memo[1][j]+memo[2][j] in E:
                if memo[0][j]=='-':memo[0][j]='o'
                elif memo[1][j]=='-':memo[1][j]='o'
                else:memo[2][j]='o'
                ans=1
        if ans==0 and memo[0][0]+memo[1][1]+memo[2][2] in E:
            if memo[0][0]=='-':memo[0][0]='o'
            elif memo[1][1]=='-':memo[1][1]='o'
            else:memo[2][2]='o'
            ans=1
        if ans==0 and memo[0][2]+memo[1][1]+memo[2][0] in E:
            if memo[0][2]=='-':memo[0][2]='o'
            elif memo[1][1]=='-':memo[1][1]='o'
            else:memo[2][0]='o'
    print('Case '+str(i+1)+':')
    for j in range(len(memo)):
        for k in range(len(memo[j])):
            print(memo[j][k],end="")
        print("")