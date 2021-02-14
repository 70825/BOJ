N=int(input())
memo=[]
D=[]
for i in range(N):
    memo.append(str(input())[::-1])
    D.append(memo[i][0])
k=1
sub_memo=D
if len(list(set(sub_memo)))==len(D):print(k)
else:
    while 1:
        for i in range(N):D[i]+=memo[i][k]
        sub_memo=D;k+=1
        if len(list(set(sub_memo)))==len(D):
            print(k)
            break