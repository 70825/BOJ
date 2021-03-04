N=str(input())
memo=[]
for i in range(len(N)):
    memo.append(int(N[i]))
if memo.count(0)!=0 and sum(memo)%3==0:
    print(''.join(map(str,sorted(memo,reverse=True))))
else:print(-1)