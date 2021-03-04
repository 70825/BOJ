memo=[]
N=int(input())
for i in range(N):
    S=input().split()
    memo.append([S[1],S[0]])
memo.sort()
for i in memo:print(i[1],i[0])