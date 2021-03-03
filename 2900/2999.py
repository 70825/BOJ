S=str(input())
memo=[]
n=1
while n!=len(S):
    if len(S)%n==0 and len(S)//n not in memo:
        memo.append(n)
    n+=1
ans=max(memo)
for i in range(ans):
    for j in range(len(S)//ans):
        print(S[j*ans+i],end="")