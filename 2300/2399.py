from sys import stdin
N=int(input())
memo=[*map(int,stdin.readline().split())]
k=0
memo.sort()
for i in range(N):
    a=len(memo[:i:1])
    b=len(memo[i:N-1:1])
    k+=abs(memo[i]*a-sum(memo[:i:1]))+abs(memo[i]*b-sum(memo[i+1::1]))
print(k)