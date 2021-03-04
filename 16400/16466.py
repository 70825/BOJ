input=__import__('sys').stdin.readline
N=int(input())
memo=sorted([*map(int,input().split())])
k=0
if memo[0]!=1:k=1
else:
    for i in range(N-1):
        if memo[i]!=memo[i+1]-1:
            k=memo[i]+1
            break
if k==0:print(memo[len(memo)-1]+1)
else:print(k)