memo=[]
sub_memo=[]
N=int(input())
for i in range(N):
    memo.append(int(input()))
memo.sort()
for i in range(N//2):
    sub_memo.append(memo[i]+memo[N-1-i])
print(min(sub_memo))