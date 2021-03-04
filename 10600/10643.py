memo=[]
sub_memo=[]
for i in range(8):
    memo.append(int(input()))
for i in range(8):
    a,b,c,d=i,i+1,i+2,i+3
    if b>7:b-=8
    if c>7:c-=8
    if d>7:d-=8
    sub_memo.append(memo[a]+memo[b]+memo[c]+memo[d])
print(max(sub_memo))