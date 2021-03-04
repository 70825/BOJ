def permutation(D):
    i,j=len(D)-1,len(D)-1
    while i >0 and D[i-1]>=D[i]:i-=1
    if i<=0:return False
    while D[i-1]>=D[j]:j-=1
    D[i-1],D[j]=D[j],D[i-1]
    j=len(D)-1
    while i<j:
        D[i],D[j]=D[j],D[i]
        i+=1;j-=1
    return True

N=int(input())
num=[*map(int,input().split())]
sub_memo=[*map(int,input().split())]
memo=[];MAX,MIN=-10**9,10**9
for i in range(4):
    for j in range(sub_memo[i]):
        memo.append(i)
memo.sort()
while 1:
    k=num[0]
    for i in range(N-1):
        if memo[i]==0:k+=num[i+1]
        elif memo[i]==1:k-=num[i+1]
        elif memo[i]==2:k*=num[i+1]
        else:
            if k<0:k=-(abs(k)//num[i+1])
            else:k//=num[i+1]
    if k>MAX:MAX=k
    if MIN>k:MIN=k
    if not permutation(memo):break
print(MAX)
print(MIN)