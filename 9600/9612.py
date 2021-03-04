memo={}
for i in range(int(input())):
    S=input()
    if S not in memo:memo[S]=1
    else:memo[S]+=1
sub_memo=sorted(memo,reverse=True)
for i in sub_memo:
    if memo[i] == memo[max(memo)]:
        print(i,memo[max(memo)]);break