n,d,k=map(int,input().split())
memo=[]
sub_memo=[]
for i in range(n):
    s,c=map(str,input().split())
    c=int(c)
    memo.append([c,s])
memo.sort(reverse=True)
money=0;ans=0
for i in range(n):
    money+=memo[i][0];ans+=1
    sub_memo.append(memo[i][1])
    if money >= d:break
if ans>k:ans=-1
if ans==-1 or money<d:print('impossible')
else:
    print(ans)
    for i in sub_memo:
        print(str(i)+', YOU ARE FIRED!')