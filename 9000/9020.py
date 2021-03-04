T=10000
Check=[0]*(T+1)
Check[0]=Check[1]=True
Prime=[]
for i in range(2,T+1):
    if not Check[i]:
        Prime.append(i)
        j = i+i
        while j<=T:
            Check[j]=True;j+=i
for i in range(int(input())):
    N=int(input())
    memo=[]
    for j in Prime:
        if Check[N-j]==False:
            memo.append([abs(N-2*j),j,N-j])
    memo.sort()
    print(memo[0][1],memo[0][2])