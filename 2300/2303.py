N=int(input())
memo=[]
for i in range(N):
    A=[*map(int,input().split())]
    ans=0
    for j in range(len(A)-2):
        for k in range(j+1,len(A)-1):
            for l in range(k+1,len(A)):
                if ans<(A[j]+A[k]+A[l])%10:
                    ans=(A[j]+A[k]+A[l])%10
    memo.append(ans)
sub_memo=[]
for i in range(N):
    if memo[i]==max(memo):
        sub_memo.append(i+1)
print(max(sub_memo))