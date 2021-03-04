n,m=map(int,input().split())
D=[*map(int,input().split())]
memo=[[0,0] for i in range(m)]
sub_memo=[]
Max=0
for i in range(m):
    solve=input().split()
    memo[i][1]=int(solve[0])
    for j in range(1,n+1):
        if solve[j]=='O':
            memo[i][0]+=D[j-1]
    if memo[i][0]>Max:Max=memo[i][0]
for i in range(m):
    if memo[i][0]==Max:
        sub_memo.append(memo[i][1])
print(min(sub_memo),Max)