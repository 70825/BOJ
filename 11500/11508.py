input=__import__('sys').stdin.readline
N=int(input())
memo=[]
for i in range(N):
    memo.append(int(input()))
memo.sort()
S=0
while len(memo)!=0:
    if len(memo)>=3:
        S+=memo[len(memo)-1]+memo[len(memo)-2]
        for i in range(3):
            del memo[len(memo)-1]
    else:
        S+=sum(memo)
        break
print(S)