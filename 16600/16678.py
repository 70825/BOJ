input=__import__('sys').stdin.readline
memo=[]
ans,k,hacker,t=1,0,0,0
N=int(input())
for i in range(N):
    memo.append(int(input()))
memo.sort()
i=0
while i!=N:
    if memo[i]==ans:ans+=1;i+=1
    elif memo[i]<ans:i+=1
    else:
        hacker+=memo[i]-ans
        memo[i]=ans
        ans+=1;i+=1
print(hacker)