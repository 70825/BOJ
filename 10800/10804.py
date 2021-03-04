memo=[]
for i in range(20):
    memo.append(i+1)
for i in range(10):
    a,b=map(int,input().split())
    for j in range((b-a+1)//2):
        temp=memo[a+j-1]
        memo[a+j-1]=memo[b-j-1]
        memo[b-j-1]=temp
print(' '.join(map(str,memo)))