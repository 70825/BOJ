n,m=map(int,input().split())
memo=[]
sub_memo=[]
for i in range(m):
    memo.append(int(input()))
result=[]
for i in range(1,2**m):
    flag = bin(i)[2:].zfill(m)
    subset=[memo[j] for j in range(m) if flag[j] == '1']
    if sum(subset)>=n:
        result.append(sum(subset))
print(min(result))