a,b=map(int,input().split())
memo=[]
for i in range(1,a+1):
    if a%i==0:memo.append(i)
if len(memo)<b:print(0)
else:print(memo[b-1])