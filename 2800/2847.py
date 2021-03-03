N=int(input())
memo=[];s=0
for i in range(N):
    memo.append(int(input()))
while 1:
    k=0
    for i in range(N-1):
        if memo[i]>=memo[i+1]:
            k+=memo[i]-(memo[i+1]-1)
            memo[i]=memo[i+1]-1
    s+=k
    if k==0:break
print(s)