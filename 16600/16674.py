N=input()
memo=[]
for i in range(len(N)):
    memo.append(int(N[i]))
sub_memo=sorted(list(set(memo)))
k=0
for i in sub_memo:
    if i not in [0,1,2,8]:k+=1
if k==0:
    if sub_memo==[0,1,2,8]:
        if memo.count(0)==memo.count(1)==memo.count(2)==memo.count(8):print(8)
        else:print(2)
    else:print(1)
else:print(0)