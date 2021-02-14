N=input()
k=0
for i in range(1,len(N)):
    memo1,memo2 =1,1
    for j in range(len(N)):
        if j<i:memo1*=int(N[j])
        else:memo2*=int(N[j])
    if memo1==memo2:k=1;break
if k==1:print('YES')
else:print('NO')